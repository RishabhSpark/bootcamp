from pathlib import Path

file_path = Path("myfile.txt")
content = file_path.read_text()

print(content)
