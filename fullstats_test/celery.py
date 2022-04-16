import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fullstats_test.settings')

app = Celery('fullstats')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'parse': {
        'task': 'main_app.tasks.parse',
        'schedule': crontab(hour='*/1'),
    }
}