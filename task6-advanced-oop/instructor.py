from person import Person

class Instructor(Person):
    """
    Represents an instructor who teaches courses.
    """

    def __init__(self, name: str, instructor_id: str):
        super().__init__(name, instructor_id)
        self._courses_taught = []

    def assign_course(self, course):
        self._courses_taught.append(course)

    def list_courses(self):
        return self._courses_taught

    def get_role(self) -> str:
        return "Instructor"