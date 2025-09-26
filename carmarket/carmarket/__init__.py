# from __future__ import absolute_import, unicode_literals
#
# # Это гарантирует, что приложение Celery загрузится при запуске Django
# from carmarket.celery import app as celery_app
#
# __all__ = ('celery_app',)

from carmarket.celery import app as celery_app

__all__ = ('celery_app',)