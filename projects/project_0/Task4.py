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

"""
    Runtime Analysis
    =======================================
    Let the number of records in texts list = m, and 
    the number of records in calls list = n

    extracting data from texts list into two separate lists = O(2m) = O(m)
    extracting data from calls list into two separate lists = O(2n) = O(n)

    creating sets for all 4 lists = 2*O(n) + 2*O(m) = O(n) + O(m)

    now, the set unique callers would contain some entries say k, where k <= n
    We iterate it to do set operation of checking if a set has an element, and we do this in 3 sets, and append conditionally and the loop runs k times
    this = O(k)

    Then we sort the list created, the size of which is say l, where l <= k,
    then we sort it, time complexity = O(l log l)

    Then we iterate it l times to print the possible telemarketers list = O(l)

    Total time complexity = 2*O(n) + 2*O(m) + O(k) + O(l log l) + O(l)
                          = O(n) + O(m) + O(k) + O(l) + O(l log l)

    But, for worst case time complexity, lets say input size is x, where x = m + n, total entries in calls and texts
    Then time complexity will be a * O(x), where a is some constant, so we ignore it,
    so the algorithm takes linear time, i.e. O(x)

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
