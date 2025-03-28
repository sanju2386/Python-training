# Solution 1: Use a raw string (r"")
path = r"C:\Users\292593\Desktop\master\python training\python_code_submit\Python-training\word.txt"

# Open file in read mode
with open(path, "r") as file:  # Corrected mode from r to "r"
    content = file.read()
    print(content)
