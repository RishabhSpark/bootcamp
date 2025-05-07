def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line  # Yield each line one by one

# Usage
for line in read_large_file("large_file.txt"):
    print(line.strip())  # Process each line
