"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from functools import reduce
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""


def find_most_common():

    numbers = {}

    for call in calls:
        if call[0] in numbers:
            numbers[call[0]] += int(call[3])
        else:
            numbers[call[0]] = int(call[3])

    for call in calls:
        if call[1] in numbers:
            numbers[call[1]] += int(call[3])
        else:
            numbers[call[1]] = int(call[3])

    greatest = (0, 0)

    for number, length in numbers.items():
        length = int(length)
        if length > greatest[1]:
            greatest = (number, length)

    return greatest


result = find_most_common()

print("{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.".format(
    telephone_number=result[0], total_time=result[1]))
