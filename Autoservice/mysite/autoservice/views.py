from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Service, Order


def index(request):
    services = Service.objects.all()
    service_count = services.count()
    cars = Car.objects.all()
    car_count = cars.count()

    # Laisvos knygos (tos, kurios turi statusą 'g')
    completed_orders_count = Order.objects.filter(status__exact='p').count()


    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'service_count': service_count,
        'car_count': car_count,
        'completed_orders_count': completed_orders_count,
    }

    response = render(request, 'index.html', context=context)
    return response

