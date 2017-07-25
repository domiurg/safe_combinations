#!/usr/bin/python

import pdb

# p1, p2, p3 - plugs in the discs
# Formula:
# p3 - p2 = b - a + 8
# p1 = p2 + b - c
# from equation system above:
# p3 - p1 = (b - a + 8) - (b - c)

# Values of the First digit
a = range(0, 10)
# Values of the Second digit
b = range(0, 10)
# Values of the Third digit
c = [1, 2, 6, 7]

count = 0
unique = []
# 3 nested loops to go over every possible combination of safe codes
# and check them for eligibility
for i in a:
    for j in b:
        for k in c:
            # Compute (b - a + 8) - (b - c) from equation above
            val = (j - i + 8) - (j - k)
            # Check if it is viable
            if val > 9:
                continue

            else:
                # initialize list of possible solutions
                found = []
                # 2 nested loops to find all combinations of p1 and p3 that satisfy equation
                for p3 in range(0, 10):
                    for p1 in range(0, 10):
                        if (p3-p1) == val:
                            found.append((p1, p3))

                if found:
                    # if i == 3 and j == 2 and k == 1:
                    #     pdb.set_trace()
                    for (p1, p3) in found:
                        p2 = p1 - (j - k)
                        if p2 in range(0, 10):
                            if (p2 != p1 + 4) and (p3 != p2 + 5):
                                count += 1
                                print '(' + str(p1) + str(p2) + str(p3) + ')' + '(' + str(i) + str(j) + str(k) + ')'
                                if (i, j, k) not in unique:
                                    unique.append((i, j, k))
                else:
                    continue

print count
print len(unique)