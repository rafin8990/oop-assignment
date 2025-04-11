class StudentDatabase:
    __student_list = []

    @classmethod
    def add_student(cls, student):
        cls.__student_list.append(student)

    @classmethod
    def get_all_students(cls):
        return cls.__student_list

    @classmethod
    def find_student_by_id(cls, student_id):
        for student in cls.__student_list:
            if student._Student__student_id == student_id:
                return student
        return None


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student {self.__student_id} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Student {self.__student_id} has been enrolled.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Student {self.__student_id} is already not enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Student {self.__student_id} has been dropped.")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"ID: {self.__student_id}, Name: {self.__name}, "
              f"Department: {self.__department}, Status: {status}")


Student("S101", "Alice Smith", "Computer Science")
Student("S102", "Bob Johnson", "Electrical Engineering", True)
Student("S103", "Charlie Brown", "Mechanical Engineering")


while True:
    print("------ Student Management System ------")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        students = StudentDatabase.get_all_students()
        if not students:
            print("No students in the database.")
        for s in students:
            s.view_student_info()

    elif choice == '2':
        sid = input("Enter student ID to enroll: ")
        student = StudentDatabase.find_student_by_id(sid)
        if student:
            student.enroll_student()
        else:
            print("Invalid student ID.")

    elif choice == '3':
        sid = input("Enter student ID to drop: ")
        student = StudentDatabase.find_student_by_id(sid)
        if student:
            student.drop_student()
        else:
            print("Invalid student ID.")

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
