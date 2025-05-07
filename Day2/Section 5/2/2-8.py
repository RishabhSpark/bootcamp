from pathlib import Path

file_path = Path("myfile.txt")

if file_path.exists() and file_path.is_file():
    print(f"{file_path} exists and is a file.")
else:
    print(f"{file_path} does not exist or is not a file.")
