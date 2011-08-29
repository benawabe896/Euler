"""By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)"""

import time, math
ti = time.time()

big_str = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".strip().splitlines()


triangle = {}
x = 0
for line in big_str:
    y = 0    
    line = line.strip().split(' ')
    for num in line:
        index = str(x) + "," + str(y)

        if index not in triangle:
            triangle[index] = {}
        triangle[index]['val'] = num
        
        parentindex = str(x - 1) + "," + str(y)
        if parentindex in triangle:
            triangle[parentindex][index] = num

        parentbackindex = str(x - 1) + "," + str(y - 1)
        if parentbackindex in triangle:
            triangle[parentbackindex][index] = num
        y += 1
    x += 1

def mather(dictionary):
    for i in reversed(xrange(14)):
        incr = 0
        while incr > -1:
            current_index = str(i) + "," + str(incr)
            if current_index not in dictionary:
                incr = -1
            else:
                current = int(dictionary[str(i) + "," + str(incr)]['val'])
                child1 = int(dictionary[str(i + 1) + "," + str(incr)]['val'])
                child2 = int(dictionary[str(i + 1) + "," + str(incr + 1)]['val'])
                if child1 > child2:
                    dictionary[current_index]['val'] = current + child1
                else:
                    dictionary[current_index]['val'] = current + child2
                incr += 1
    return dictionary['0,0']['val']
                
def recurse(x, y, dictionary):
    current_index = str(x) + "," + str(y)
    
    if len(dictionary[current_index]) == 1:
        return int(dictionary[current_index]['val'])
    
    left = recurse(x + 1, y, dictionary)
    right = recurse(x + 1, y + 1, dictionary)

    if left > right:
        return int(dictionary[current_index]['val']) + left
    else:
        return int(dictionary[current_index]['val']) + right
        
print recurse(0, 0, triangle)
#print mather(triangle)

print "Time taken(secs):", time.time() - ti
