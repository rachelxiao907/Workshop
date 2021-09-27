# Rachel Xiao, Eliza Knapp, Thomas Yu
# SoftDev
# K05 -- Better Living Through Amalgamation/Combining Code/Found the best way to print a random student name from each period between me, Eliza, and Thomas.
# 2021-09-26

# SUMMARY OF TRIO DISCUSSION
#   FIRST ATTEMPT
#   After looking at all three of our files, we decided that it would be easiest
#   to read the names off of two separate text files, one for period 1 and the
#   other for period 2. The generate_name function takes in each of those files
#   and tries to open it (uses try and except courtesy of Thomas' group). It adds the
#   contents to a list, shuffles it, and prints the first index. If opening
#   the files or looking at their content is not possible, it prints the according
#   error message.
# DISCOVERIES
#   - We learned how to use try: and except: in python (none of us took Annual CS).
#   - I learned how to read a file and store its information in a list.
#   - We learned what a dictionary is and how to access the keys and its items.
# QUESTIONS
#   - Should we print or return the names inside of the function?
#   - How might we change the code to make it run for infinite periods of students?
#   - Is the runtime of shuffle significantly longer than random.randint for longer lists?
# COMMENTS
#   - Although it is faster to generate a random integer and take that index of the
#   array than shuffling, we ended up going with random.shuffle(array) because
#   it looks prettier in the code and the lists aren't too long.
#   - UPDATE: we are now generating a random integer

import random

def generate_name():
    NAMES = {
        'pd1': ["Emma Buller", "Julia Nelson", "Owen Yaggy", "Haotian Gao", "Reng Zheng", "Kevin Cao", "Michelle Lo", "Ivan Lam", "Christopher Liu", "Lucas Lee"],
        'pd2': ["Jesse Xie", "Rachel Xiao", "Yuqing Wu", "Liesel Wong", "Josephine Lee", "Yaying Liang", "Justin Zou", "Patrick Ging", "Raymont Yueng", "Michael Borczuk", "Eliza Knapp", "Thomas Yu", "Jonathan Wu", "Andy Lin", "Andrew Juang", "Annabel Zhang", "David Chong"]
    }
    
    #get a random index from each list 
    index1 = random.randint(0, len(NAMES['pd1'])-1) #randint is inclusive
    index2 = random.randint(0, len(NAMES['pd2'])-1)
    
    #print the names and period
    print("pd1: " + NAMES['pd1'][index1])
    print("pd2: " + NAMES['pd2'][index2])

generate_name()
