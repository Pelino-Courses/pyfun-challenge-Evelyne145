from abc import ABC, abstractmethod

class Person(ABC):
    """
    Base class for people in the university system.
    Everyone has a name and an ID.
    """

    def __init__(self, name: str, person_id: str):
        self.name = name
        self.person_id = person_id

    @abstractmethod
    def get_role(self) -> str:
        """Every person should be able to say who they are (Student, Instructor, etc.)."""
        pass

    def __str__(self):
        return f"{self.name} (ID: {self.person_id})"
    