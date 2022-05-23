from django.db import models
from django.urls import reverse
import uuid


class CarModel(models.Model):
    car_brand = models.CharField('Brand', max_length=100, null=False)
    car_model = models.CharField('Model', max_length=100, null=False)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.car_brand} {self.car_model}'

    class Meta:
        verbose_name = 'Car Model'
        verbose_name_plural = 'Car Models'


class Car(models.Model):
    country_registration_no = models.CharField('Country registration number', max_length=100, null=False)
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT, null=False)
    vin_code = models.CharField('VIN', max_length=100)
    client = models.CharField('Client\'s full name',
                              max_length=100,
                              null=False,
                              help_text='Client name and surname')

    def __str__(self):
        return f'{self.country_registration_no} {self.car_model} {self.vin_code} {self.client}'

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])


class Service(models.Model):
    service_name = models.CharField('Service name', max_length=100, null=False)
    price = models.FloatField('Price', null=False)

    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.service_name}'

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Order(models.Model):
    order_date = models.DateField('Order Date', null=False)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=False)
    order_amount = models.FloatField('Order Amount', null=False)

    ORDER_STATUS = (
        ('p', 'processing'),
        ('c', 'completed'),
        ('r', 'rejected'),
    )

    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        blank=True,
        default='p',
        help_text='Order status',
    )

    class Meta:
        ordering = ['order_date']

    def __str__(self):
        return f'{self.id} ({self.order_date}) ({self.car.car_model})'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def display_service(self):
        return ', '.join(orderlines.service.service_name for orderlines in self.orderlines.all())

    display_service.short_description = 'Service'

    def display_quantity(self):
        return ', '.join(str(orderlines.quantity) for orderlines in self.orderlines.all())

    display_quantity.short_description = 'Quantity'

    def display_price(self):
        return ', '.join(str(orderlines.price) for orderlines in self.orderlines.all())

    display_price.short_description = 'Price'


class OrderLine(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT, null=False)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False, related_name='orderlines')
    quantity = models.IntegerField('Quantity', null=True)
    price = models.FloatField('Price', null=False)

    def __str__(self):
        return f'{self.id} {self.service.service_name} {self.quantity} {self.price}'

    class Meta:
        verbose_name = 'Order Line'
        verbose_name_plural = 'Order Lines'
