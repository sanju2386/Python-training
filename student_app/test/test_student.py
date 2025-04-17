import unittest
from student_manager import StudentManager
from student import Student

class TestStudentManager(unittest.TestCase):

    def setUp(self):
        self.manager = StudentManager()

    def test_add_student(self):
        student = self.manager.add_student("Ponnu", 13, "A++")
        self.assertEqual(len(self.manager.students), 1)
        self.assertEqual(student.name, "Ponnu")

    def test_find_student_by_id(self):
        student = self.manager.add_student("Bincy", 13, "A+")
        found = self.manager.find_student_by_id(student.student_id)
        self.assertEqual(found.name, "Bincy")

if __name__ == '__main__':
    unittest.main()
