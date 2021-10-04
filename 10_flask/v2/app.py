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

app.run()

# Predictions:
# This will print two lines in terminal: The first line is "about to print __name__". The second line is "__main__".
# Returns No hablo queso! to the home directory of website.

# Results:
# After loading the website, the program met the predictions. The lines are printed in the terminal after loading the website.