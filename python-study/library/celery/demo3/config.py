from datetime import timedelta

CELERY_TIMEZONE='Asia/Shanghai'
CELERY_ENABLE_UTC=True
CELERY_IMPORTS=('tasks',)
CELERY_RESULT_BACKEND='amqp'
#CELERY_RESULT_BACKEND='db+sqlite://C:/Users/zhoufan/Desktop/result.db'
'''
CELERYBEAT_SCHEDULE={
    'add-every-30-secods':{
        'task':'tasks.add',
        'schedule':timedelta(seconds=3),
        'args':(16,16)
    },
}
print 'config end'
'''