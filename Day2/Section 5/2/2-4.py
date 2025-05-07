import os
import shutil
from pathlib import Path

# Create a temporary directory
temp_dir = Path("temp_dir")
os.makedirs(temp_dir, exist_ok=True)

# Create a temporary file inside the directory
temp_file = temp_dir / "temp_file.txt"
temp_file.write_text("Temporary file content")

# Delete the temporary directory safely with its content
shutil.rmtree(temp_dir)
