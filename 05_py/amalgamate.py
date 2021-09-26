# Rachel Xiao
# SoftDev
# K05 -- Amalgamate/Combining Code/Found the best way to print a random student name from each period between me, Eliza, and Thomas.
# 2021-09-24

# Summary:
# Discoveries:
# Questions:
# Comments:

import random

#function to get a random name from the list of names
def randomName(arr):
    length = len(arr)
    index = random.randint(0, length-1) #inclusive
    #print(index)
    print(arr[index])

pd1 = ["Emma Buller", "Julia Nelson", "Owen Yaggy", "Haotian Gao", "Reng Zheng", "Kevin Cao", "Michelle Lo", "Ivan Lam", "Christopher Liu"]
randomName(pd1)

pd2 = ["Jesse Xie", "Rachel Xiao", "Yuqing Wu", "Liesel Wong", "Josephine Lee", "Yaying Liang", "Justin Zou", "Patrick Ging", "Raymond Yueng", "Michael Borczuk"]
randomName(pd2)

