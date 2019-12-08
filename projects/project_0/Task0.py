"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('./texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('./calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# i am not considering the time required to read from the files and store the data in lists

# constant time to read the records, as len() has O(1) complexity
first_text_record = texts[0]
last_call_record = calls[len(calls) - 1]

# format() scans a text and does replacements, the replacements will be as much as the number of arguments for format()
print("First record of texts, {} texts {} at time {}".format(
    first_text_record[0], first_text_record[1], first_text_record[2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
    last_call_record[0], last_call_record[1], last_call_record[2], last_call_record[3]))

# so, overall, my part of code will have a linear complexity, O(1)
