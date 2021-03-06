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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# filtering out calls made by people from banglore
banglore_calls = [call for call in calls if call[0][0:5] == "(080)"]

banglore_calls_area_codes = []
banglore_calls_mobile_prefixes = []


for call in banglore_calls:
    if (call[1][0] == "7") or (call[1][0] == "8") or (call[1][0] == "9"):
        banglore_calls_mobile_prefixes.append(call[1][0:4])
    elif call[1][0:2] == "(0":
        banglore_calls_area_codes.append(call[1][0: (call[1].find(')') + 1)])


unique_banglore_area_codes = set(banglore_calls_area_codes)
unique_banglore_calls_mobile_prefixes = set(banglore_calls_mobile_prefixes)

# PART A
print("The numbers called by people in Bangalore have codes:\n")
for area_code in sorted(list(unique_banglore_area_codes.union(unique_banglore_calls_mobile_prefixes))):
    print(area_code)

# PART 2
fixed_to_fixed_count = 0
for call in banglore_calls:
    if call[1][0:5] == "(080)":
        fixed_to_fixed_count += 1

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    round(((fixed_to_fixed_count*100)/len(banglore_calls)), 2)))
