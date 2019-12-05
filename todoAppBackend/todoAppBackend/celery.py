from __future__ import absolute_import
 
 
from celery import Celery
import os
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoAppBackend.settings.dev') #Nota 1
from django.conf import settings  # Nota 2
 
app = Celery('todoAppBackend') #Nota 3
 
app.config_from_object('django.conf:settings') #Nota 4
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #Nota 5
 
app.conf.update(
    BROKER_URL = 'redis://localhost:6379/10', #Nota 6
)