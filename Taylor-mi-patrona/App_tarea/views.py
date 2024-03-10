from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_context = {'username': 'Templates y archivos estáticos'}
    return render(request, 'App_tarea\index.html', context=my_context)
    