from django.contrib import admin
from .models import CarModel, Car, Service, Order, OrderLine


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    readonly_fields = ('id',)
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_service', 'display_quantity', 'display_price', 'order_date', 'car', 'status', 'due_back',
                    'user')
    list_editable = ('status', 'due_back')
    list_filter = ('status', 'due_back')
    inlines = [OrderLineInline]

    # fieldsets = (
    #     (None, {
    #         'fields': ('car', 'id')
    #     }),
    #     ('Availability', {
    #         'fields': ('status', 'due_back', 'user')
    #     }),
    # )


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'client', 'country_registration_no', 'vin_code')
    list_filter = ('client', 'car_model__car_brand', 'car_model__car_model')
    search_fields = ('country_registration_no', 'vin_code')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'price')


admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)


