"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
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
call_duration_records = dict()

for record in calls:
    if record[0] in call_duration_records:
        call_duration_records[record[0]] += int(record[3])
    else:
        call_duration_records[record[0]] = int(record[3])

    if record[1] in call_duration_records:
        call_duration_records[record[1]] += int(record[3])
    else:
        call_duration_records[record[1]] = int(record[3])


max_caller_duration = 0
max_caller_number = ""

for number in call_duration_records:
    if call_duration_records[number] > max_caller_duration:
        max_caller_duration = call_duration_records[number]
        max_caller_number = number

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    max_caller_number, max_caller_duration))
