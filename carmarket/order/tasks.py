from celery import shared_task
from django.utils import timezone
from datetime import timedelta

from order.models import Order, Sale
from showroom.models import Showroom
from car.models import Car
from user.models import Seller, Buyer



def order_by_showroom(id_showroom: int, model: str) -> None:
    """"
    buy the same model of car from a seller, that the buyer bought from a showroom
    """
    showroom = Showroom.objects.get(pk=id_showroom)
    users = {i.user_id: i.id for i in showroom.seller.all()}
    discounts = {i.seller.id: i.discount for i in Sale.objects.filter(showroom=id_showroom)}
    cars = []

    for car in Car.objects.filter(user__in=users.keys()):

        if not car.is_active or car.model != model:
            continue

        price = car.price

        if car.user_id in discounts:
            price = car.price * discounts[car.user_id] / 100

        cars.append((car, price))

    car, price = min(cars, key=lambda x: x[1])

    showroom.balance -= price
    showroom.save()
    seller_id = users[car.user_id]
    seller = Seller.objects.get(pk=seller_id)
    seller.balance += price
    seller.save()
    car.delete()
    Order.objects.create(model=model, description="buy_car_in_seller",
                  price=price, showroom=showroom,
                  seller=seller)


@shared_task
def from_showroom_to_seller_task():

    now = timezone.now()
    time = now - timedelta(minutes=10)

    orders_by_buyer = Order.objects.filter(
        created_at__range=(time, now),
        seller__isnull=True
    )

    if not orders_by_buyer:
        return {"message": "there have been no orders for the last ten minutes"}

    for order in orders_by_buyer:
        model = order.model
        id_showroom = order.showroom.id
        order_by_showroom(id_showroom, model)

    return {"message": "orders executed"}


@shared_task
def chose_best_seller():
    """"
    chosing the best seller for showroom
    """
    result = []
    for showroom in Showroom.objects.all():
        best_seller = "No discount"
        max_discount = 0
        for seller in showroom.seller.all():
            now = timezone.now()
            try:
                sale = Sale.objects.get(
                    showroom=showroom,
                    seller=seller,
                    date_start__lte=now,
                    date_end__gte=now
                )
            except Sale.DoesNotExist:
                continue
            if sale.discount > max_discount:
                max_discount = sale.discount
                best_seller = seller.username
        result.append((showroom.username, best_seller, max_discount))
    return {"message": result}


descript = 'buy car throught offer'

@shared_task
def offer_task(user_id, model, max_price):
    """
    selling car from showroom to buyer
    """

    buyer = Buyer.objects.get(user_id=user_id)

    if buyer.balance >= max_price:
        car = Car.objects.filter(model=model, price__lte=max_price,
                                 user_id__in=Showroom.objects.all().values_list("user_id", flat=True), is_active=True
                                 ).order_by('price')[0]

        if car:
            car.is_active = False
            car.save()
            buyer.balance -= car.price
            buyer.save()
            showroom = Showroom.objects.get(user_id=car.user.id)
            Order.objects.create(model=model, description=descript,
                                         price=car.price, buyer=buyer,
                                         showroom=showroom)
            car.delete()
            return {"message": "offer success"}
        return {"message": "there are no suitable cars available"}
    return {"message": "there are no money"}