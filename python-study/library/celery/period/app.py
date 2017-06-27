#encoding:gbk
from celery import Celery
import config

app=Celery()
app.config_from_object(config)
print app.conf.CELERY_TIMEZONE
