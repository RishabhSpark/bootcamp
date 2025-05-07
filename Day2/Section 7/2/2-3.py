import csv

def filter_csv(file_path, condition):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if condition(row):  # Check if row meets the condition
                yield row  # Yield the row if condition is met

# Usage
def is_valid_row(row):
    return len(row) > 2  # Example condition: row must have more than 2 elements

for row in filter_csv('data.csv', is_valid_row):
    print(row)
