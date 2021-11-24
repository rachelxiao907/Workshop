# Wandering Wolverine: Rachel Xiao, Wen Hao Dong
# SoftDev pd2
# K19 -- A RESTful Journey Skyward
# 2021-11-23
# time spent: 45 minutes

from flask import Flask, render_template
from urllib import request
import json

app = Flask(__name__)

KEY = ""
with open("key_nasa.txt", "r") as key_file:
    KEY = key_file.read()

@app.route("/")
def disp_page():
    page = request.urlopen(f"https://api.nasa.gov/planetary/apod?api_key={KEY}") #f string to add key to the url
    #print(page)
    url_dict = json.loads(page.read()) #turns the reading of the link which uses JSON format into a dictionary
    #print(url_dict)
    #print(url_dict['url'])
    return render_template('main.html', pic=url_dict['url'], explanation=url_dict['explanation'])

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
