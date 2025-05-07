from pathlib import Path

# List all Python files in the current directory
python_files = Path(".").glob("*.py")

for file in python_files:
    print(file)