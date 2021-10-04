# Team Polar: Yuqing Wu, Jesse Xie, Rachel Xiao
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

# Predictions:
# The Debug mode is turned on in the terminal. This will Print debug information in the terminal.
# The program will print two lines in terminal and "No hablo queso!" to the website.

#Results:
# * Debug mode: on
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 429-585-123
# about to print __name__...
# __main__
# 127.0.0.1 - - [04/Oct/2021 09:13:02] "GET / HTTP/1.1" 200 -

# The debugger in the terminal detects a change and prints the terminal after saving new edits to the program.
# * Detected change in '/Users/yuqingwu/softdev/workshop/10_flask/v3/app.py', reloading
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 429-585-123

# When the code is run but has an error in it, the debugger specifies the error on the website.
# The website gives more information about the error with the Werkzeug powered traceback interpreter.
# In the terminal, the error and the line of error is printed. The traceback is also printed. Ex:
# pri(__name__)   #where will this go?
# NameError: name 'pri' is not defined

# Without the debugger, the website will display an "Internal Server Error".
