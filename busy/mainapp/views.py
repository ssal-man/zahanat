from django.shortcuts import render
from .models import Bus
from django.views.decorators.csrf import csrf_exempt

def index(request):
    context = {'buses' : Bus.objects.all()}
    return(render(request, 'mainapp/base.html', context))

@csrf_exempt
def buslist(request):
    if request.method == "GET": 
        context = {'buses' : Bus.objects.all()}
        return(render(request, 'mainapp/base.html', context))
    elif request.method == "POST":
        context = {'test' : 'This is post request'}
        return(render(request, 'mainapp/base.html', context))
    