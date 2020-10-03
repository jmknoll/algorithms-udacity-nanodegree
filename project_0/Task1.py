"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

uniques = set()
for text in texts:
    uniques.add(text[0])
    uniques.add(text[1])
for call in calls:
    uniques.add(call[0])
    uniques.add(call[1])

print("There are {number} different telephone numbers in the records.".format(
    number=len(uniques)))
