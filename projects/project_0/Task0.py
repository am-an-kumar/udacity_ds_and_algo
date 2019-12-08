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

"""
    Runtime analysis
    =========================
    The entries in the csv files are already sorted w.r.t time, so the lists are already sorted w.r.t time.
    Getting an element in a list using indexing is a O(1) operation.
    Getting the length of python list is also a O(1) operation as lists store their length as meta data.
    String.format() does formatting in O(1) time as the format() has only a few string substitutions to do and it does not depend on the input size as we are doing this for 1 enty in each file.

    Time complexity = O(n)

"""

print("First record of texts, {} texts {} at time {}".format(
    texts[0][0], texts[0][1], texts[0][2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
    calls[len(calls)-1][0], calls[len(calls)-1][1], calls[len(calls)-1][2], calls[len(calls)-1][3]))
