# Rachel Xiao
# SoftDev
# Classwork0/Random Student Name Using Lists/Created two lists for students in period 1 and 2. Printed a random student name from each period
# 2021-09-21

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
