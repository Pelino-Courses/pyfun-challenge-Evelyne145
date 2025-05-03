class EnrollmentError(Exception):
    pass

class EnrollmentManager:
    """
    Manages enrollments between students and courses.
    """

    def __init__(self):
        self.enrollments = []

    def enroll(self, student, course):
        if student in course.students:
            raise EnrollmentError(f"{student.name} is already enrolled in {course.name}.")
        student.enroll(course)
        course.enroll_student(student)
        self.enrollments.append((student, course))