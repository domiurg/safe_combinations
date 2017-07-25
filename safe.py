#!/usr/bin/python

import pdb

# p1, p2, p3 - plugs in the discs
# Formula:
# p3 - p2 = b - a + 8
# p1 = p2 + b - c
# from equation system above:
# p3 - p1 = (b - a + 8) - (b - c)
# p2 = p1 - (b - c)

# Values of the First digit
a = range(0, 10)
# Values of the Second digit
b = range(0, 10)
# Values of the Third digit
c = [1, 2, 6, 7]

count = 0
unique = []

file = open("combinations_list.txt", "w")
file.write("Combinations List\n")
file.write("Safe\tPeg\t\tKey\n")

file1 = open("unique_combinations_list.txt", "w")
file1.write("Combinations List\n")
file1.write("Safe\tPeg\t\tKey\n")

comb = []

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
                # Initialize list of possible solutions
                found = []
                # 2 nested loops to find all combinations of p1 and p3 that satisfy equation
                for p3 in range(0, 10):
                    for p1 in range(0, 10):
                        if (p3-p1) == val:
                            found.append((p1, p3))
                # If solutions for p1 and p3 were found check further
                if found:
                    for (p1, p3) in found:
                        # Compute p2 from equation above
                        p2 = p1 - (j - k)
                        # Check if p2 is viable
                        if p2 in range(0, 10):
                            # Check for slots with opposite physical positions (Pic_1, Fig_#2)
                            if (p2 != (p1 + 5) % 10) and (p3 != (p2 + 5) % 10):
                                # Count total number of solutions
                                count += 1
                                comb.append(((i,j,k),(p1,p2,p3)))
                                line = '(' + str(i) + str(j) + str(k) + ')\t(' + str(p1) + str(p2) + str(p3) + ')\t' +\
                                       str(k)
                                # Print to standard output
                                print line
                                # Write to output file
                                file.write(line+'\n')
                                # Count total number of unique safe combinations
                                if (i, j, k) not in unique:
                                    unique.append((i, j, k))
                else:
                    continue
u_count = 0
u_comb = []
for item in comb:
    c = 0
    for i in comb:
        if item[0] == i[0]:
            c += 1
    if c == 1:
        u_count += 1
        u_comb.append(item)

file.close()
# Print total number of combinations
print count
print len(comb)
# Print Unique number of combinations
print len(unique)

print u_count
for i in u_comb:
    line = '(' + str(i[0][0]) + str(i[0][1]) + str(i[0][2]) + ')\t(' + str(i[1][0]) + str(i[1][1]) + str(i[1][2]) +\
           ')\t' + str(i[0][2])
    print line
    file1.write(line+'\n')

