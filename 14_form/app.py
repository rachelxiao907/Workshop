# Team Marshmallow: Liesel Wong (King Hagrid), Yoonah Chang (Yelena), Rachel Xiao (Mooana)
# SoftDev
# K14 -- Form and Function
# 2021-10-14 

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future self and/or current teammates understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) # <Flask 'app'>
    print("***DIAG: request obj ***")
    print(request) # <Request 'http://127.0.0.1:5000/' [GET]> --after submitting form--> <Request 'http://127.0.0.1:5000/auth?username=hello&sub1=Submit+Query' [GET]>
                   # request shows the url of the localhost when tracking the form data
    print("***DIAG: request.args ***")
    print(request.args) # ImmutableMultiDict([]) --> ImmutableMultiDict([('username', 'hello'), ('sub1', 'Submit Query')])  |  (this creates a dictionary with
                        # [name of input tag: user input] 
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username']) # hello  |  (this prints the inputted username)
    print("***DIAG: request.headers ***")
    print(request.headers) # Host: 127.0.0.1:5000
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return "Waaaa hooo HAAAH"  #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
