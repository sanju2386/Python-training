import random

used_ids = set()

def generate_unique_id():
    while True:
        new_id = random.randint(1000, 9999)
        if new_id not in used_ids:
            used_ids.add(new_id)
            return str(new_id)

class Student:
    def __init__(self, name, age, grade, student_id=None):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id if student_id else generate_unique_id()

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }


    @staticmethod
    def from_dict(data):
        return Student(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            grade=data["grade"]

        )
    
if __name__ == "__main__":
    main()
    