import os
from celery import Celery

# Set default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('personal_shopping_assistant')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()