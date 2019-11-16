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
        return(render(request, 'mainapp/buslist.html', context))
    elif request.method == "POST":
        context = {}
        return(render(request, 'mainapp/buslist.html', context))
    

def details(request, bus, bpoint):
    context = {
        'bus' : bus,
        'bpoint' : bpoint
    }
    return(render(request, 'mainapp/details.html', context))
    