with open("Day2/Section 2/4/example.txt", "r") as f1, open("Day2/Section 2/4/example_copy.txt", "w") as f2:
    data = f1.read()
    f2.write(data)