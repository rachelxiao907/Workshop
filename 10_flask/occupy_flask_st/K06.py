# Team Polar: Yuqing Wu, Jesse Xie, Rachel Xiao
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04

import csv
import random

job_classes = []
percentages = []

with open('occupations.csv') as csv_file: # give access to the file by opening it
    reader = csv.reader(csv_file, delimiter=',') # delimeter puts values in a list for each row as it splits by commas
    for row in reader:
        if row[0] != "Job Class" and row[0] != "Total": # don't store the heading or total
            job_classes.append(row[0])
            percentages.append(float(row[1]))

def main(): # occupation-chooser
    # we pick the occupation from the list job_classes with the weighted percentages and we only pick one
    mixed = random.choices(job_classes, weights=percentages, k=1) # creates a list of size k
    return mixed[0]