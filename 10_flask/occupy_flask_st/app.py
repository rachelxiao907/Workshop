# Team Polar: Yuqing Wu, Jesse Xie, Rachel Xiao
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04

from flask import Flask
import K06
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    
    heading = '''Team Polar: Yuqing Wu, Jesse Xie, Rachel Xiao <br/>
    SoftDev <br/>
    K10 -- Putting Little Pieces Together<br/>
    2021-10-04 <br/><br/>'''
    return heading + K06.main() + "<br/>\n<br/>" + str(K06.job_classes)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()