from rest_framework import serializers
from mainapp.models import BPoint,Bus,BusLoc,Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Route
        fields='__all__'

class BusLocSerializer(serializers.ModelSerializer):
    bno=serializers.CharField(source='get_bno')
    class Meta:
        model=BusLoc
        fields='__all__'
        read_only_fields=('bno',)

class BusSerializer(serializers.ModelSerializer):
    lat = serializers.FloatField(source='get_lat')
    long = serializers.FloatField(source='get_long')
    class Meta:
        model=Bus
        fields='__all__'
        read_only_fields=('lat', 'long',)

class BPointSerializer(serializers.ModelSerializer):
    class Meta:
        model=BPoint
        fields='__all__'