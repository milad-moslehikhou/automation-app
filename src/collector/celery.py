import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automation_app.settings')
app = Celery('automation_app')
app.conf.update(
    broker_url='redis://{}:6379/0'.format(os.environ.get("REDIS_HOST", default='localhost')),
    result_backend='redis://{}:6379/0'.format(os.environ.get("REDIS_HOST", default='localhost')),

    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    track_started=True,
)
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
