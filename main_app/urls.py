from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CardModelViewSet

routers = DefaultRouter()
routers.register(r'cards', CardModelViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]