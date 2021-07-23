from rest_framework.response import Response
from task.models import Provider, Service
from .serializers import ProviderSerializer, ServiceSerializer
from rest_framework import status
from rest_framework import generics
from django.core import serializers
from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.gis.db import models
from geojson import Polygon


def index(request):
    providers = Provider.objects.all()
    serializer = ProviderSerializer(instance=providers)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


class listProviders(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class CreateProvider(generics.CreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class UpdateProvider(generics.RetrieveUpdateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class DeleteProvider(generics.DestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class listServices(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class CreateService(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class UpdateService(generics.RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class DeleteService(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class listOneService(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'name'
    


def api_get_utm(request, name):
    utm_poly = serialize('geojson', Service.objects.all(), geometry_field='location', fields=('name', 'price', 'provider'))
    return HttpResponse(utm_poly, content_type='application/json')
    lookup_field = 'name'



class allServs(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        longitude = self.request.query_params.get('longitude')
        latitude= self.request.query_params.get('latitude')
        location = Polygon(longitude, latitude)
        queryset = Service.objects.all()

        return queryset