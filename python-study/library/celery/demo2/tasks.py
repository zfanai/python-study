#encoding:gbk
from celeryapp import app

# ����task��task()������
@app.task()
def add(x, y):
    result = x + y
    print result
    return result