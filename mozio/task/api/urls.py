from django.urls import path, include
from . import views
from .views import index, listProviders, listServices, listOneService, api_get_utm, allServs, CreateProvider, UpdateProvider, DeleteProvider, CreateService, UpdateService, DeleteService
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

router = DefaultRouter()
router.register(r'allServs', views.allServs , basename='Service')
urlpatterns = router.urls

urlpatterns = [
    path("", index),
    path("providers", listProviders.as_view()),
    path("services", listServices.as_view()),
    path("service/<str:name>", listOneService.as_view()),
    path('utm/<str:name>', views.api_get_utm, name='utm'),
    url(r'^', include(router.urls)),
    path("createprovider", CreateProvider.as_view()),
    path("updateprovider/<int:pk>", UpdateProvider.as_view()),
    path("deleteprovider/<int:pk>", DeleteProvider.as_view()),
    path("createservice", CreateService.as_view()),
    path("updateservice/<int:pk>", UpdateService.as_view()),
    path("deleteservice/<int:pk>", DeleteService.as_view()),
]