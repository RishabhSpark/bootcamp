import os

def read_file_lbyl(file_name: str) -> str:
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return file.read()
    else:
        return "File not found."

file_name = "test_file.txt"
print(read_file_lbyl(file_name))  # This could fail if another process deletes the file after the check.