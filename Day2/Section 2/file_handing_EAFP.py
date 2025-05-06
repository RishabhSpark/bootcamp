def read_file_eafp(file_name: str) -> str:
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

print(read_file_eafp("non_existent_file.txt"))