from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Service, Order, OrderLine
from django.shortcuts import render, get_object_or_404
from django.views import generic


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


def cars(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    response = render(request, 'cars.html', context=context)
    return response


def car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    response = render(request, 'car.html', {'car': car})
    return response


class OrderListView(generic.ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'order_list.html'

    def get_queryset(self):
        return Order.objects.filter(status='p')


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
