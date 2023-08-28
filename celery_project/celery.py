from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app=Celery('celery_project')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings,namespace='CELERY')
app.conf.beat_sehedule ={
    
}
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'request:{self.request!r}')