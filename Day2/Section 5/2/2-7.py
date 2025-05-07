from pathlib import Path

relative_path = Path("myfile.txt")
absolute_path = relative_path.resolve()

print(f"Absolute path: {absolute_path}")
