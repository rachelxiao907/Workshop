import random

#function to get a random name from the list of names
def randomName(arr):
    length = len(arr)
    index = random.randint(0, length-1) #inclusive
    #print(index)
    print(arr[index])

pd1 = ["Emma Buller", "Julia Nelson", "Owen Yaggy", "Haotian Gao", "Reng Zheng"]
randomName(pd1)

pd2 = ["Jesse Xie", "Rachel Xiao", "Yuqing Wu", "Liesel Wong", "Josephine Lee", "Yaying Liang", "Justin Zou"]
randomName(pd2)
