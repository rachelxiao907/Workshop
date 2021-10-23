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


students_file = csv.DictReader(open("students.csv")) # values in the first row are the keys of the dict
courses_file = csv.DictReader(open("courses.csv"))
# for row in students_file: # check how the dictionary reader looks like
#    print(row)

# CREATE TABLE IF NOT EXIST bypasses the error of TABLE ALREADY EXISTS
command = "CREATE TABLE students(name TEXT, age INTEGER KEY, id INTEGER PRIMARY KEY);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement
for row in students_file:
    command = "INSERT INTO students VALUES(row['name'], row['age'], row['id'])"
    c.execute(command)

command1 = "CREATE TABLE IF NOT EXIST courses(code TEXT, mark INTEGER KEY, id INTEGER PRIMARY KEY);"
command2 = "SELECT * FROM students;"

#c.execute(command1)
c.execute(command2)

#==========================================================

db.commit() #save changes
db.close()  #close database
