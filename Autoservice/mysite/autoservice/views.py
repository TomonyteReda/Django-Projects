from django.http import HttpResponse

def index(request):
    return HttpResponse("Autoservice Project")

