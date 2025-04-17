from student import Student
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        student = Student(name, age, grade)
        self.students.append(student)
        return student

    def get_all_students(self):
        return self.students

    # def find_student_by_id(self, student_id):
    #     return next((s for s in self.students if s.student_id == student_id), None)
    def find_student_by_id(self,student_id):
        for students in self.students:
            if students.student_id == student_id:
                return students
        return None


    def delete_student(self, student_id):
        student = self.find_student_by_id(student_id)
        if student:
            self.students.remove(student)
            return True
        return False