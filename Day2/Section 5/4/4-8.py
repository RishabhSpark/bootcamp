import csv
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])

# Read CSV file into namedtuples
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        person = Person(*row)
        print(person)
