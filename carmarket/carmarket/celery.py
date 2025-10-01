import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carmarket.settings')


app = Celery('carmarket')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'from_showroom_to_seller_task': {
#         'task': 'order.tasks.from_showroom_to_seller_task',
#         'schedule': 60,
#     }
# }