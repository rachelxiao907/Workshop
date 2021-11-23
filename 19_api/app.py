# Wandering Wolverine: Rachel Xiao, Wen Hao Dong
# SoftDev pd2
# K19 -- A RESTful Journey Skyward
# 2021-11-23
# time spent: 1 hour

from flask import Flask, render_template
from urllib import request
import json

app = Flask(__name__)

@app.route("/")
def disp_page():
    page = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=Bh5EFULUqcQmnVqskzAFlyrq3d4Ubw6vcIzsIq30")
    print(page)
    url_dict = json.loads(page.read())
    print(url_dict['url'])
    return render_template('main.html', pic=url_dict['url'], explanation=url_dict['explanation'])

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
