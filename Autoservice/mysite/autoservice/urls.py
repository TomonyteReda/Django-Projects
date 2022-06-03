from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:car_id>', views.car, name='car'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order_details'),
    path('search/', views.search, name='search'),
    path('myorders/', views.OrdersByUserListView.as_view(), name='my_orders'),
    path('register/', views.register, name='register')
]


