# coding: gbk
from celery import Celery

#BROKER_URL = 'redis://:password@localhost:6379/0'
#BACKEND_URL = 'redis://:password@localhost:6379/1'

#BROKER_URL = 'redis://localhost:6379/0'
#BACKEND_URL = 'redis://localhost:6379/1'
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
#BACKEND_URL = 'amqp://guest:guest@localhost:5672//'
BACKEND_URL = 'amqp://'

# Add tasks here
CELERY_IMPORTS = (
    'tasks',
)

app = Celery('celery',
    broker=BROKER_URL,
    backend=BACKEND_URL,
    include=CELERY_IMPORTS,)

app.conf.update(

    #CELERY_ACKS_LATE=True,
    #CELERY_ACCEPT_CONTENT=['pickle', 'json'],
    #CELERYD_FORCE_EXECV=True,
    #CELERYD_MAX_TASKS_PER_CHILD=500,
    #BROKER_HEARTBEAT=0,
)