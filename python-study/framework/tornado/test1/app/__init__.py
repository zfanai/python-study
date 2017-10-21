import time
from flask import Flask


app=Flask(__name__)

@app.route('/')
def index():
    #time.sleep(3600)
    return '<html>index</html>'
    

@app.route('/age')
def age():
    return '<html>age:30</html>'    