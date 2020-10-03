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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def sends_or_recieves_texts(number):
    for text in texts:
        if text[0] == number or text[1] == number:
            return True
    return False


def recieves_calls(number):
    for call in calls:
        if call[1] == number:
            return True
    return False


suspected = set()

for call in calls:
    if not sends_or_recieves_texts(call[0]) and not recieves_calls(call[0]):
        suspected.add(call[0])

suspected = sorted(suspected)
print("These numbers could be telemarketers:")
for suspect in suspected:
    print(suspect)
