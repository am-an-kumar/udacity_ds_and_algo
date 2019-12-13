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
text_receivers = []
text_senders = []

for record in texts:
    text_senders.append(record[0])
    text_receivers.append(record[1])

unique_text_receivers = set(text_receivers)
unique_text_senders = set(text_senders)

callers = []
callees = []

for record in calls:
    callers.append(record[0])
    callees.append(record[1])

unique_callers = set(callers)
unique_callees = set(callees)

possible_telemarketers = []

for caller in unique_callers:
    if((caller not in unique_text_receivers) and (caller not in unique_text_senders) and (caller not in unique_callees)):
        possible_telemarketers.append(caller)

print("These numbers could be telemarketers: \n")
for caller in sorted(possible_telemarketers):
    print(caller)
