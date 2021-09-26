# Rachel Xiao, Eliza Knapp, Thomas Yu
# SoftDev
# K05 -- Amalgamate/Combining Code/Found the best way to print a random student name from each period between me, Eliza, and Thomas.
# 2021-09-26

'''
Summary:
    After looking at all three of our files, we decided that it would be easiest
    to read the names off of two separate text files, one for period 1 and the
    other for period 2. The generate_name function takes in each of those files
    and tries to open it (uses try and except courtesy of Thomas' group). It adds the
    contents to a list, shuffles it, and prints the first index. If opening
    the files or looking at their content is not possible, it prints the according
    error message.

Discoveries:
    - We learned how to use try: and except: in python (none of us took Annual CS).
    - I learned how to read a file and store its information in a list.

Questions:
    - Should we print or return the names inside of the function?
    - How might we change the code to make it run for infinite periods of students?
    - Is the runtime of shuffle significantly longer than random.randint for longer lists?

Comments:
    - Although it is faster to generate a random integer and take that index of the
    array than shuffling, we ended up going with random.shuffle(array) because
    it looks prettier in the code and the lists aren't too long.

'''

import random

def generate_name(pd1_file, pd2_file):
    pd1 = []
    pd2 = []

    #pd1
    try:
        pd1_names = open(pd1_file)
        for line in pd1_names:
            pd1.append(line.strip())
        pd1_names.close()

        try:
            random.shuffle(pd1)
            print("pd1: " + pd1[0])
        except:
            print("Pd1 text file is empty")
    except:
        print("The pd1 file doesn't exist")

    #pd2
    try:
        pd2_names = open(pd2_file)
        for line in pd2_names:
            pd2.append(line.strip()) #strip removes the \n at the end of each line
        pd2_names.close()

        try:
            random.shuffle(pd2)
            print("pd2: " + pd2[0])
        except:
            print("Pd2 text file is empty")
    except:
        print("The pd2 file doesn't exist")

generate_name("pd1.txt", "pd2.txt")
