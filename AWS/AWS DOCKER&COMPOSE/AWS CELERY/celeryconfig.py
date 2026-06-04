#1. From project file where settings.py file is create celery.py file and add this configurations:
from celery import Celery
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

app = Celery("config")

app.config_from_object(
    "django.conf:settings",
    namespace="CELERY"
)

app.autodiscover_tasks()


#2 from project folder alter __init__.py by adding this configuration
from .celery import app as celery_app

__all__ = ("celery_app",)


#3 install celery and redis and include it in requirements.py file

pip install Celery
pip install redis


#4 include configuration in settings.py file:

CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0" 
#notice 'redis' must match the service name in docker-compose container



#5 create a tasks.py file in django app and include logic

from celery import shared_task

@shared_task
def add(x, y):
    return x + y

#6 add celery workers service to compose

celery:
  build: .
  command: celery -A config worker -l info
  depends_on:
    - redis
    - db

docker compose up -d --build

//Debug on terminal on web service manage.py shell to confirm all is working :
>> import shoppit.tasks
>>> from celery import current_app
>>> current_app.tasks.keys()

//COMMANDLINES TO CONFIRM ALL IS WORKING
docker compose restart celery
docker compose logs -f celery
docker compose logs celery


ALGORICAL PROCESS FOR INTEGRATION:

🎯 TASK 4

Complete:

1.

Install Celery

2.

Configure Redis broker

3.

Create celery.py

4.

Create add() task

5.

Add worker service to compose

6.

Run:

docker compose up --build
7.

Execute:

add.delay(4, 6)
8.

Verify task execution in Celery logs