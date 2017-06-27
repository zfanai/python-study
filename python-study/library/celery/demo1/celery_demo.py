#encoding:gbk

from celery import Celery

app=Celery('tasks', backend='redis://127.0.0.1:6379/1',broker='redis://127.0.0.1:6379/0')

'''
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=[''],
    CELERY_RESULT_SERIALIZE='json',
    CELERY_ENABLE_UTC=True
) '''

@app.task
def add(x,y):
    return x+y

if __name__=='__main__':
    add.delay(4,4)
