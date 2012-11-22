"""Pennies"""

import time, math, itertools, sys

ti = time.time()

#n = 7
#print n * (n + 1)**2 / 2
#print n * (n + 2) * (2*n - 1) / 8
#print n * (n + 2) * (2*n - 1) / 8
#sys.exit()

def getfirst(strip):
    global gold, penny, blank

    incr = 0

    for ch in strip:
        if ch != blank:
            return {incr : ch}
        incr+= 1

def getlast(strip):
    global gold, penny, blank

    incr = 1

    for ch in strip[::-1]:
        if ch != blank:
            return {len(strip) - incr : ch}
        incr+= 1

def num_options(strip_length, num_pennies):
    n = strip_length - num_pennies
    total = n
    for i in range(1,num_pennies + 1):
         total *= (n + i)
    total = total / math.factorial(num_pennies)
    return total
    
def avail_moves(strip):
    global gold, penny, blank

    first = getfirst(strip)
    last = getlast(strip)
    prev_coin = blank
    prev_pos = len(strip)
    new_strips = {}
    
    for incr in reversed(xrange(len(strip))):
        if incr in last:
            """nothing"""
        if incr < last:
            new_strip = strip[:]
            if strip[incr] == blank and prev_coin != blank:
                new_strip = new_strip[:incr] + prev_coin + new_strip[incr + 1:]
                new_strip = new_strip[:prev_pos] + blank + new_strip[prev_pos + 1:]
                new_strips[new_strip] = True
            else:
                if incr in first:
                    new_strip = new_strip[:incr] + blank + new_strip[incr + 1:]
                    new_strips[new_strip] = True
        if strip[incr] != blank:
            prev_coin = strip[incr]
            prev_pos = incr
    return new_strips

def winorlose(strip):
    global gold, penny, blank, winning_strips, losing_strips

    #print strip
    if strip in winning_strips:
        #print "<------" + "Winning Match"
        return "Winning"
        
    if strip in losing_strips:
        #print "<------" + "Losing Match"
        return "Losing"
        
    if strip in choice_strips:
        #print "<------" + "Losing Match"
        return "Choice"
        
    if gold not in strip:
        losing_strips[strip]  = True
        #print "<------" + "Losing No Gold"
        return "Losing"

    getfirstarray = getfirst(strip)
    for gf in getfirstarray:
        if getfirstarray[gf] == gold:
            winning_strips[strip] = True
            #print "<------" + "Winning, first is gold"
            return "Winning"
    
    available_moves = avail_moves(strip)

    if len(available_moves) == 1 and strip[1] == gold:
        losing_strips[strip] = True
        #print "<------" + "Losing, force brings gold to first"
        return "Losing"

    tmp_status = 'None'
    winning_incr = 0
    losing_incr = 0
    for move in available_moves:
        verdict = winorlose(move)
        if verdict == 'Losing':
            losing_incr += 1
        if verdict == "Winning":
            winning_incr += 1
        if verdict == 'Choice':
            winning_incr += 1
            
    if winning_incr > 0 and losing_incr == 0:
        losing_strips[strip] = True
        return "Losing"
    if winning_incr == 0 and losing_incr > 0:
        winning_strips[strip] = True
        return "Winning"
    if winning_incr > 0 and losing_incr > 0:
        choice_strips[strip] = True
        return "Choice"
    
    return tmp_status
    
#print avail_moves('ooxOx')

gold = 'O'
penny = 'o'
blank = 'x'

num_golds = 1
num_pennies = 2
num_strip = 12

winning_strips = {}
losing_strips = {}
choice_strips = {}

#print "Final Result: " + winorlose('xoO')


for P in range(num_pennies + 1):
    for B in range(1,num_strip + 1):
        strip = []
        for i in range(num_golds):
            strip.append(gold)
        for i in range(P):
            strip.append(penny)
        for i in range(B - num_golds - P):
            strip.append(blank)

        uniques = {}

        incr = 0
        for i in itertools.permutations(strip):
            tmp_strip = ''
            for ch in i:
                tmp_strip += ch
            uniques[tmp_strip] = True
            incr += 1 


        for unique in uniques.keys():
            result = winorlose(unique)
            #print "Unique - " + unique + " result: " + result
            if result == 'Winning' or result == 'Choice':
                winning_strips[unique] = True
            if result == 'Losing':
                losing_strips[unique] = True 
                
#print winning_strips
#print losing_strips

total_winning_strips = {}
total_losing_strips = {}

for ws in winning_strips:
    current_golds = 0
    current_blanks = 0
    current_pennies = 0
    
    for ch in ws:
        if ch == gold:
            current_golds += 1
        if ch == blank:
            current_blanks += 1
        if ch == penny:
            current_pennies += 1
    if current_golds == num_golds and current_blanks == (num_strip - num_golds - num_pennies) and current_pennies == num_pennies:
        total_winning_strips[ws] = True

for ls in losing_strips:
    current_golds = 0
    current_blanks = 0
    current_pennies = 0
    
    for ch in ls:
        if ch == gold:
            current_golds += 1
        if ch == blank:
            current_blanks += 1
        if ch == penny:
            current_pennies += 1
    if current_golds == num_golds and current_blanks == (num_strip - num_golds - num_pennies) and current_pennies == num_pennies:
        total_losing_strips[ls] = True

#print total_winning_strips
#print total_losing_strips
print "Winning Strips: " + str(len(total_winning_strips))
print "Losing Strips: " + str(len(total_losing_strips))

#print uniques.keys()
#print len(uniques)
#print incr

#num_options(1000000,100)
    
print "Time taken(secs):", time.time() - ti
