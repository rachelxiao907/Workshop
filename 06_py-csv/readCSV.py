# TEAM POLAR - Rachel Xiao, Jesse Xie, Yuqing Wu
# Soft Dev
# K06 -- StI/O: Divine Your Destiny!/Read CSV Files/Python script that reads file, stores data in a dictionary, and randomly selects occupations based on their percentages
# 2022-09-28

# SUMMARY
#   We read the occupations CSV file by storing each row as a list. The first index of each list would be
#   the keys in the dictionaries and the second index of each list would be the item of each corresponding
#   key. Then, we randomly selected a number between 0 and the total percentage so we can decrement by the
#   weighted percentages as we iterate through the dictionary. When the total percentage reaches 0 or is
#   less than that, the corresponding occupation is printed. This works because the decrement of a random
#   number within the total percentage gives every occupation a random chance.
# DISCOVERIES
#   - delimeter=',' is like s.split(",") in Java
# QUESTIONS
#   - Is there a better way to randomly select an occupation with its weighted percentage?

import csv
import random

occupations = {}

with open('occupations.csv') as csv_file: #give access to the file by opening it
    reader = csv.reader(csv_file, delimiter=',') #delimeter puts values in a list for each row as it splits by commas
    for row in reader:
        if row[0] != "Job Class": #don't store the heading
            occupations[row[0]] = float(row[1]) #put the data in a dictionary    
#print(occupations)

def select_occupation(occupations):
    #pick a random number less than the total percentage
    total = random.uniform(0.0, occupations["Total"]) #excludes the total
    #print(total)
    for key, value in occupations.items():
        total -= value #decrement random total percentage until you can't anymore
        if(total <= 0):
            print(key)
            break
    
select_occupation(occupations)