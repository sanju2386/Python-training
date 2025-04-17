from student_manager import StudentManager
from storage import Storage  # Make sure to import Storage correctly

def menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search by ID")
    print("4. Delete Student")
    print("5. Exit")

def main():
    storage = Storage()  # Create an instance of the Storage class
    manager = StudentManager()

    data = storage.load_from_file()  # Load data from file using the storage instance
    manager.load_students(data)  # Initialize manager with data

    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == '1':
            # Add student
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            student = manager.add_student(name, age, grade)
            print(f"Student added with ID: {student.student_id}")
        
        elif choice == '2':
            # View all students
            students = manager.get_all_students()
            if not students:
                print("No students found.")
            else:
                for s in students:
                    print(s.to_dict())

        elif choice == '3':
            # Search student by ID
            sid = input("Enter Student ID: ")
            student = manager.find_student_by_id(sid)
            print(student.to_dict() if student else "Student not found.")

        elif choice == '4':
            # Delete student
            sid = input("Enter Student ID to delete: ")
            if manager.delete_student(sid):
                storage.save_to_file(manager.export_students())  # Save updated list
                print("Deleted successfully.")
            else:
                print("Student not found.")
        
        elif choice == '5':
            # Exit and save data
            storage.save_to_file(manager.export_students())  # Ensure data is saved before exiting
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
