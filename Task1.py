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
unique_tele_nums = set()

for call in calls:
    unique_tele_nums.add(call[0])
    unique_tele_nums.add(call[1])   
    
for txt in texts:
    unique_tele_nums.add(txt[0])
    unique_tele_nums.add(txt[1]) 
  
print("There are " + str(len(unique_tele_nums)) + " different telephone numbers in the records.")