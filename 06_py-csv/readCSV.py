# Rachel Xiao
# Soft Dev
# K06 -- StI/O: Divine Your Destiny!/Read CSV Files/Python script that reads file, stores data in a dictionary, and randomly selects occupations based on their percentages
# 2022-09-28

import csv
import random

occupations = {}

with open('occupations.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',') #delimeter makes values in a list after each comma
    for row in reader:
        if row[0] != "Job Class" and row[1] != "Percentage":
            occupations[row[0]] = float(row[1]) #put the data in a dictionary
            
#print(occupations)

def select_occupation(occupations):
    #pick a random number less than the total percentage
    total = random.uniform(0.0, occupations["Total"]) #excludes the total
    for key, value in occupations.items():
        total -= value #decrement random total percentage until you can't anymore
        if(total <= 0):
            print(key)
            break
    
select_occupation(occupations)