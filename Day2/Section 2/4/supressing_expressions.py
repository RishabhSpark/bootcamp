from contextlib import suppress

with suppress(FileNotFoundError):
    with open("non_existent_file.txt", "r") as f:
        data = f.read()