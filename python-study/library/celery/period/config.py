from datetime import timedelta

CELERY_TIMEZONE='Asia/Shanghai'
CELERY_ENABLE_UTC=True
CELERY_IMPORTS=('tasks',)
CELERYBEAT_SCHEDULE={
    'add-every-30-secods':{
        'task':'tasks.add',
        'schedule':timedelta(seconds=3),
        'args':(16,16)
    },
}
print 'config end'