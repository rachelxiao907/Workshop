# Team KingMlob: Liesel Wong, Yaying Liang, Rachel Xiao (Duckies: King Hagrid, Blob, and Mooana)
# SoftDev
# K13 -- Template for Success
# 2021-10-08

from flask import Flask, render_template
import csv
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

occupations = {}

with open('data/occupations.csv') as csv_file: #give access to the file by opening it
    ''' Access the occupations.csv file so we can read the data in Python. Adds to a dictionary with the jobs as keys and a list of percentage and link as values. '''
    reader = csv.reader(csv_file, delimiter=',') #delimeter puts values in a list for each row as it splits by commas
    for row in reader:
        if row[0] != "Job Class": #don't store the heading or total
            occupations[row[0]] =[float(row[1]), row[2]] #put the data in a dictionary. job: [percent, link]
            
def make_choice():
    ''' Uses the dictionary data to return a random occupation based on its weighted percentages. '''
    jobs = list(occupations.keys()) #convert the keys into a list
    jobs.pop(len(jobs)-1) #remove the "Total" index
    
    values = list(occupations.values()) #creates a list of lists using dict values [ [percent, link], [percent, link], ... ]
    values.pop(len(values)-1) #remove the "Total" index
    percentages = []
    for arr in values:
        percentages.append(arr[0]) #store the weighted percentages in a list
    choice = random.choices(jobs, weights=percentages, k=1) #create a list of with the random occupation
    return choice[0]

@app.route("/occupyflaskst")
def test_tmplt():
    ''' Generates output from a template file by giving inputs '''
    return render_template('tablified.html', dict = occupations, selected_occupation = make_choice())

if __name__ == "__main__":
    app.debug = True
    app.run()