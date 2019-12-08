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

"""
    Runtime Analysis
    ===========================
    Lets say texts list has "m" records, while calls has "n" records

    First for loop for texts = O(m)
    Second for loop for calls = O(n)
    {Assuming list append is of O(1) complexity}

    Set constructor to filter out duplicate records will take each entry and insert it if it does not exist already, this will take O(1) to check if it exists already or not, and O(1) to add if it does not exist already. Therefore,
    Set constructor = O(m+n)

    overall complexity = O(m) + O(n) + O(m+n)
    But, we can approximate it to O(x) where x = m + n, as 2 * O(n) = O(n)
"""

all_numbers = []
# grabbing numbers from text records
for record in texts:
    all_numbers.append(record[0])
    all_numbers.append(record[1])

# grabbing numbers from call records
for record in calls:
    all_numbers.append(record[0])
    all_numbers.append(record[1])

# filtering out duplicate numbers
unique_numbers = set(all_numbers)
print(
    "There are {} different telephone numbers in the records.".format(len(unique_numbers)))
