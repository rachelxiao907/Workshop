# Team Marshmallow: Rachel Xiao (Mooana), Liesel Wong (King Hagrid), Yoonah Chang (Yelena)
# SoftDev
# K16 -- All About Database
# 2021-10-22

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


students_file = csv.DictReader(open("students.csv")) # values in the first row are the keys of the dict for each row
# for row in students_file: # check how the dictionary reader looks like
#   print(row) # {'name': 'alison', 'age': '23', 'id': '10'}
# CREATE TABLE IF NOT EXIST bypasses the error of TABLE ALREADY EXISTS
c.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, id INTEGER);")    # create students table
for lines in students_file: # loop through each dictionary in reader
    c.execute("INSERT INTO students VALUES(\"" + lines['name'] + "\"," + lines['age'] + "," + lines['id'] + ")") # populate the table by concatenating the variables into the command String
    # \" is used to signify that lines['name'] is type TEXT

courses_file = csv.DictReader(open("courses.csv"))
c.execute("CREATE TABLE IF NOT EXISTS courses (code TEXT, mark INTEGER, id INTEGER);")    # create courses table
for lines in courses_file:
    c.execute("INSERT INTO courses VALUES(\"" + lines['code'] + "\"," + lines['mark'] + "," + lines['id'] + ")")

#==========================================================

db.commit() #save changes
db.close()  #close database
