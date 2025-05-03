from person import Person

class Student(Person):
    """
    Represents a student.
    Students can enroll in courses.
    """

    def __init__(self, name: str, student_id: str):
        super().__init__(name, student_id)
        self._courses = []

    def enroll(self, course):
        self._courses.append(course)

    def list_courses(self):
        return self._courses

    def get_role(self) -> str:
        return "Student"