class Course:
    """
    Represents a course.
    Has a name, code, and an optional instructor.
    """

    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code
        self.instructor = None
        self.students = []

    def __str__(self):
        return f"{self.code} - {self.name}"

    def assign_instructor(self, instructor):
        self.instructor = instructor

    def enroll_student(self, student):
        self.students.append(student)

    def __iter__(self):
        """Custom iterator to loop through enrolled students."""
        return iter(self.students)
    