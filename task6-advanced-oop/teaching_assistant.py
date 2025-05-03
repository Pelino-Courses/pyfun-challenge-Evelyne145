from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    """
    A TA is both a student and an instructor assistant.
    Inherits from both!
    """

    def __init__(self, name: str, ta_id: str):
        Student.__init__(self, name, ta_id)
        Instructor.__init__(self, name, ta_id)

    def get_role(self) -> str:
        return "Teaching Assistant"