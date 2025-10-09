import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carmarket.settings')


app = Celery('carmarket')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()



app.conf.beat_schedule = {
    'buy_car_by_showroom': {
        'task': 'order.tasks.buy_car_by_showroom',
        'schedule': 60,
    },
    'chose_best_seller': {
        'task': 'order.tasks.chose_best_seller',
        'schedule': 65,
    }
}