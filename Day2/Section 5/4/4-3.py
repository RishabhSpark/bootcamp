import csv

with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
