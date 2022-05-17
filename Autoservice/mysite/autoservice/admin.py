from django.contrib import admin
from .models import CarModel, Car, Service, Order, OrderLine


admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderLine)


