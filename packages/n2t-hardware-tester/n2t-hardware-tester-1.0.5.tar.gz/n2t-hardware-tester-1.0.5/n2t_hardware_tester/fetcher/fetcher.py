import os.path
from dataclasses import dataclass
from typing import List, Protocol

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

from n2t_hardware_tester.authutil.auth_util import auth_on_google_classroom
from n2t_hardware_tester.n2tconfig import DOWNLOAD_FOLDER


@dataclass
class StudentSubmission:
    student_id: str
    submission_id: str
    submission_file_name: str
    turn_in_timestamp: str


class IHomeworkFetcher(Protocol):
    def get_assignment_submissions(self, course_code: str, coursework_id: str):
        pass


class ClassroomFetcher:
    def get_assignment_submissions(self, course_code: str, coursework_code: str):
        creds = auth_on_google_classroom()
        service = build("classroom", "v1", credentials=creds)
        course = self._get_course_by_code(service, course_code)
        course_students = self._get_course_students(service, course)
        coursework = self._get_coursework_by_course_and_code(
            service, course, coursework_code
        )

        homework_folder, student_submissions = self._download_submissions(
            service, course, coursework
        )
        return (
            homework_folder,
            student_submissions,
            course["id"],
            coursework["id"],
            course_students,
            coursework["dueDate"],
            coursework["dueTime"],
        )

    def _get_coursework_by_course_and_code(self, service, course, coursework_code):
        courseworks = (
            service.courses()
            .courseWork()
            .list(courseId=course["id"])
            .execute()["courseWork"]
        )
        for cw in courseworks:
            if coursework_code in cw["alternateLink"]:
                return cw
        print("CourseWork not Found")

    def _get_course_students(self, service, course) -> List[str]:
        course_id = course["id"]
        all_students = []
        page_token = None
        while True:
            students = (
                service.courses()
                .students()
                .list(courseId=course_id, pageToken=page_token)
                .execute()
            )
            all_students.extend(students["students"])
            if "nextPageToken" not in students or students["nextPageToken"] is None:
                break
            page_token = students["nextPageToken"]
        return all_students

    def _get_course_by_code(self, service, course_code: str) -> str:
        try:
            # Call the Classroom API
            results = service.courses().list().execute()
            courses = results.get("courses", [])

            if not courses:
                print("Course by code can't be found")
            for course in courses:
                alternate_link = course["alternateLink"]
                code_substring_start_index = alternate_link.rfind("/") + 1
                if alternate_link[code_substring_start_index:] == course_code:
                    return course

        except HttpError as error:
            print("An error occurred: %s" % error)

    def _download_submissions(self, service, course, coursework):
        submissions = (
            service.courses()
            .courseWork()
            .studentSubmissions()
            .list(courseId=course["id"], courseWorkId=coursework["id"])
            .execute()
            .get("studentSubmissions", [])
        )
        download_folder = os.path.join(DOWNLOAD_FOLDER)
        download_folder = os.path.join(download_folder, course["id"], coursework["id"])
        _ = os.path.dirname(download_folder)
        os.makedirs(_, exist_ok=True)

        downloaded_student_submissions = []

        creds = auth_on_google_classroom()
        drive_service = build("drive", "v3", credentials=creds)
        for submission in submissions:
            if (
                # todo - uncomment this
                # submission["state"] == "TURNED_IN"
                # and
                len(submission["assignmentSubmission"])
                > 0
            ):
                attachments = submission["assignmentSubmission"].get("attachments", [])
                attachment = attachments[0]
                file_id = attachment["driveFile"]["id"]
                file_title = attachment["driveFile"]["title"]

                request = drive_service.files().get_media(fileId=file_id)
                filename = os.path.join(download_folder, file_title)

                _ = os.path.dirname(filename)
                os.makedirs(_, exist_ok=True)

                with open(filename, "wb") as f:
                    downloader = MediaIoBaseDownload(f, request)
                    done = False
                    while done is False:
                        status, done = downloader.next_chunk()
                turn_in_time = self._get_turn_in_time_from_submission(submission)
                downloaded_student_submissions.append(
                    StudentSubmission(
                        submission["userId"],
                        submission["id"],
                        file_title[: file_title.rfind(".")],
                        turn_in_time,
                    )
                )
        return download_folder, downloaded_student_submissions

    def _get_turn_in_time_from_submission(self, submission):
        submission_history = submission["submissionHistory"]
        last_turned_in_state = None
        for submission_event in reversed(submission_history):
            if (
                "stateHistory" in submission_event
                and submission_event["stateHistory"]["state"] == "TURNED_IN"
            ):
                last_turned_in_state = submission_event
        if last_turned_in_state is None:
            return None
        return last_turned_in_state["stateHistory"]["stateTimestamp"]
