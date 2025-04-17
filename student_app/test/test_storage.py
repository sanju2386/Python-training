import unittest
from storage import Storage
from student import Student
import os
import json

class TestStorage(unittest.TestCase):

    def setUp(self):
        """Setup a fresh Storage instance"""
        self.storage = Storage(filepath="test_students.json")

    def test_save_to_file(self):
        student = Student("John", 20, "A")
        self.storage.save_to_file([student.to_dict()])
        self.assertTrue(os.path.exists("test_students.json"))

    def test_load_from_file(self):
        student = Student("John", 20, "A")
        self.storage.save_to_file([student.to_dict()])
        data = self.storage.load_from_file()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "John")

    def test_load_empty_file(self):
        if os.path.exists("test_students.json"):
            os.remove("test_students.json")
        data = self.storage.load_from_file()
        self.assertEqual(data, [])

if __name__ == '__main__':
    unittest.main()
