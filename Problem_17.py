"""215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?"""

import time, math
ti = time.time()

Small = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen',
    '20' : 'twenty',
    '30' : 'thirty',
    '40' : 'forty',
    '50' : 'fifty',
    '60' : 'sixty',
    '70' : 'seventy',
    '80' : 'eighty',
    '90' : 'ninety'
}


def num2text(n):
    words = []
    n = str(n)

    if len(n) >= 1:
        if len(n) < 2 or n[-2] != '1':
            if n[-1] in Small:
                words.append(Small[n[-1]])
    if len(n) >= 2:
        if n[-2:] in Small:
            words.append(Small[n[-2:]])
        else:
            if n[-2] in Small:
                words.append(Small[n[-2] + '0'])
    if len(n) >= 3:
        if n[-3] in Small:
            if len(words) > 0:
                words.append('and')
            words.append(Small[n[-3]] + 'hundred')
    if len(n) == 4:
        words = ['onethousand']
    return words

total = 0
for i in range(1,1001):
    for word in num2text(i):
        print "length %d word %s" % (len(word), word)
        total += len(word)

print total
print "Time taken(secs):", time.time() - ti



