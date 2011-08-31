"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?"""

import time, csv, sys, string
ti = time.time()

def letter_position(letter):
    ucase = string.uppercase
    pos = ucase.find(letter.upper()) + 1
    if pos:
        return pos

names = {}
for row in csv.reader(open('Problem_22_names.txt', 'rb')):
    for name in row:
        name_sum = 0
        for ch in name:
            name_sum += letter_position(ch)
        names[name] = name_sum

total = 0
incr = 1

for name in sorted(names.iterkeys()):
    total += names[name] * incr
    incr += 1

print total
print "Time taken(secs):", time.time() - ti
