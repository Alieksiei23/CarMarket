from django.contrib import admin

from order.models import Order, Sale

admin.site.register(Order)
admin.site.register(Sale)
