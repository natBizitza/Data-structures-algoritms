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

outgoing = []

#get all outgoing calls
for call in calls:
    if call[0]:
        outgoing.append(call[0])
        
#remove duplicates  
outgoingNoDupl = list(dict.fromkeys(outgoing)) 

for call in calls:
    if call[1] in outgoingNoDupl:
        outgoingNoDupl.remove(call[1])
        
for txt in texts:
    if txt[0] in outgoingNoDupl:
        outgoingNoDupl.remove(txt[0])
    if txt[1] in outgoingNoDupl:
        outgoingNoDupl.remove(txt[1])
        
result = sorted(outgoingNoDupl)     
print("These numbers could be telemarketers: ")
for res in result:
    print(res)
        
