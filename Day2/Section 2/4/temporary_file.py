import tempfile

with tempfile.TemporaryFile(mode="w+t") as temp_file:
    temp_file.write("Hello, temporary file!")
    temp_file.seek(0)
    print(temp_file.read())