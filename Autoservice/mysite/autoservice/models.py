from django.db import models
from django.urls import reverse
import uuid


class CarModel(models.Model):
    car_brand = models.CharField('Brand', max_length=100, null=False)
    car_model = models.CharField('Model', max_length=100, null=False)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.brand} {self.model}'


class Car(models.Model):
    country_registration_no = models.CharField('Country registration number', max_length=100, null=False)
    car_model = models.ForeignKey(CarModel, on_delete=models.RESTRICT, null=False)
    vin_code = models.CharField('VIN', max_length=100)
    client = models.CharField('Country registration number',
                              max_length=100,
                              null=False,
                              help_text='Client name and surname')

    def __str__(self):
        return f'{self.country_registration_no} {self.carmodel.car_model} {self.carmodel.car_brand} {self.vin_code}'

    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])


class Service(models.Model):
    service_name = models.CharField('Service name', max_length=100, null=False)
    price = models.FloatField('Price', null=False)

    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.service_name} {self.price}'


class Order(models.Model):
    order_date = models.DateField('Order Date', null=False)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT, null=False)
    order_amount = models.FloatField('Order Amount', null=False)

    class Meta:
        ordering = ['order_date']

    def __str__(self):
        return f'{self.id} ({self.order_date}) ({self.car.car_model})'


class OrderLine(models.Model):
    service = models.ForeignKey(Service, on_delete=models.RESTRICT, null=False)
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, null=False)
    quantity = models.IntegerField('Quantity', null=True)
    price = models.FloatField('Price', null=False)

    def __str__(self):
        return f'{self.id} {self.service.service_name} {self.service.quantity} {self.service.price}'
