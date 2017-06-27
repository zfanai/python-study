#encoding:gbk
from celeryapp import app

# 好像task和task()都可以
@app.task()
def add(x, y):
    result = x + y
    print result
    return result