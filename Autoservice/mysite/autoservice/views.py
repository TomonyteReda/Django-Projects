from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Service, Order, OrderLine
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from .forms import ClientReviewForm
from django.views.generic.edit import FormMixin


def index(request):
    services = Service.objects.all()
    service_count = services.count()
    cars = Car.objects.all()
    car_count = cars.count()

    # Laisvos knygos (tos, kurios turi statusą 'g')
    completed_orders_count = Order.objects.filter(status__exact='p').count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1


    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'service_count': service_count,
        'car_count': car_count,
        'completed_orders_count': completed_orders_count,
        'num_visits': num_visits,
    }

    response = render(request, 'index.html', context=context)
    return response


def cars(request):
    paginator = Paginator(Car.objects.all(), 1)
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)
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
    paginate_by = 1
    context_object_name = 'order_list'
    template_name = 'order_list.html'

    def get_queryset(self):
        orders = Order.objects.filter(status='p')
        return orders


class OrdersByUserListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'my_orders.html'
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).orders_in_progress().order_by_due_date()


class OrderDetailView(FormMixin, generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
    form_class = ClientReviewForm

    class Meta:
        ordering = ['order_date']

    # nurodome, kur atsidursime komentaro sėkmės atveju.
    def get_success_url(self):
        return reverse('order_details', kwargs={'pk': self.object.id})

    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # štai čia nurodome, kad knyga bus būtent ta, po kuria komentuojame, o vartotojas bus tas, kuris yra prisijungęs.
    def form_valid(self, form):
        form.instance.order = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(OrderDetailView, self).form_valid(form)


def search(request):
    query = request.GET.get('query')
    search_results = Car.objects.filter(Q(client__icontains=query) | Q(car_model__car_brand__icontains=query)
                                        | Q(country_registration_no__icontains=query) | Q(vin_code__icontains=query) \
                                        | Q(car_model__car_model__icontains=query))
    return render(request, 'search.html', {'cars': search_results, 'query': query})


@csrf_protect
def register(request):
    error_message = None
    if request.method != "POST":
        return render(request, 'register.html')

    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password != password2:
        error_message = 'Passwords do not match!'
    elif User.objects.filter(username=username).exists():
        error_message = f'User name {username} already exists'
    elif User.objects.filter(email=email).exists():
        error_message = f'User email {email} already exists'

    if error_message:
        messages.error(request, error_message)
        return redirect('register')

    User.objects.create_user(username=username, email=email, password=password)

    return render(request, 'register.html')
