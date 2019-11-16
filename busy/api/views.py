from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import BPointSerializer,BusLocSerializer,BusSerializer,RouteSerializer
from mainapp.models import BPoint,Bus,BusLoc,Route

class BPointViewSet(viewsets.ModelViewSet):
    serializer_class=BPointSerializer
    def get_queryset(self):
        queryset=BPoint.objects.all()
        r=self.request.query_params.get('routes','')
        if r:
            return queryset.filter(routes=r)
        return queryset 

class BusViewSet(viewsets.ModelViewSet):
    serializer_class=BusSerializer
    queryset=Bus.objects.all() 

class BusLocViewSet(viewsets.ModelViewSet):
    serializer_class=BusLocSerializer
    queryset=BusLoc.objects.all() 

class RouteViewSet(viewsets.ModelViewSet):
    serializer_class=RouteSerializer
    queryset=Route.objects.all()         
