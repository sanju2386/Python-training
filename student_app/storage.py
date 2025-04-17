import json
import os

class Storage(object):
    # If you want a fixed file path (as per your original design), keep it like this.
    FILE_PATH = r"C:\Users\292593\Desktop\master\python training\python_code_submit\Python-training\student_app\students.json"

    def __init__(self, filepath=None):
        # Allows overriding the default path if provided
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = self.FILE_PATH

    def save_to_file(self, data):
        #"""Saves data to the specified file."""
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"✅ Student data saved to: {self.filepath}")
        print(json.dumps(data, indent=4))

    def load_from_file(self):
        """Loads data from the specified file."""
        if not os.path.exists(self.filepath):
            return []  # Return empty list if file does not exist

        with open(self.filepath, 'r') as f:
            data = json.load(f)
            print(f"✅ Student data loaded from: {self.filepath}")
            return data


# Test functionality when running the script directly
if __name__ == "__main__":
    pass