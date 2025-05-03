
from student import Student
from instructor import Instructor
from course import Course
from enrollment import EnrollmentManager
from teaching_assistant import TeachingAssistant

def run_university_demo():
    print("🎓 Welcome to University Enrollment System Demo")

    alice = Student("Alice", "S1001")
    bob = Instructor("Dr. Bob", "I2002")
    charlie = TeachingAssistant("Charlie", "TA3003")

    cs101 = Course("Intro to Computer Science", "CS101")
    math200 = Course("Linear Algebra", "MATH200")

    cs101.assign_instructor(bob)

    em = EnrollmentManager()
    em.enroll(alice, cs101)
    em.enroll(charlie, cs101)

    print(f"\n📚 Course: {cs101}")
    print("👩‍🎓 Enrolled students:")
    for student in cs101:
        print(f"  - {student}")

    print(f"\n👨‍🏫 Instructor: {cs101.instructor}")
    print(f"🧑‍💼 Teaching Assistant Role: {charlie.get_role()}")

if __name__ == "__main__":
    run_university_demo()