# Team Marshmallow: Liesel Wong (King Hagrid), Yoonah Chang (Yelena), Rachel Xiao (Mooana)
# SoftDev
# K15 -- Sessions Greetings
# 2021-10-18

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           #facilitate flask sessions


app = Flask(__name__)    #create Flask object
app.secret_key = "SoftDev is so fun" #sign session cookies for protection against cookie data tampering
username = "topher" #hardcode username and password
password = "mykolyk"


@app.route("/") #, methods=['GET', 'POST']
def disp_loginpage():
    #Root route loads welcome page if user is logged in or login page if no user is logged in
    #print(session.items())
    if username in session: #checks if user is logged in
        return render_template('response.html', username=username) #welcome page
    else:
        return render_template('login.html') #load login page if user isn't logged in


@app.route("/auth", methods=['GET', 'POST']) #handle both GET and POST requests
def authenticate():
    #user's inputs
    name = ""
    pas = ""

    if request.method == 'GET': #if request method is GET , use request.args
        name = request.args['username']
        pas = request.args['password']
    elif request.method == 'POST':
        name = request.form['username']
        pas = request.form['password']

    #check credentials and render welcome or error page
    try:
        if name != username and pas != password:
            return render_template('login.html', explain="Username and Password are wrong")
        elif name != username:
            return render_template('login.html', explain="Username is wrong")
        elif pas != password:
            return render_template('login.html', explain="Password is wrong")
        else:
            #add session data
            session[username] = password #when a user logs in, a session should be established with the username stored
            return render_template('response.html', username=request.args['username'])  #response to a form submission
    except: #handle all unexpected errors
        return render_template('login.html', explain="something went wrong :(")


@app.route("/logout")
def logout():
    if username in session:
        #print(session.items())
        session.pop(username)
        #print(session.items()) #the dictionary is empty
    return render_template('login.html')


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
