from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CustomUserModelViewSet

routers = DefaultRouter()
routers.register(r'custom_users', CustomUserModelViewSet)


urlpatterns = [
    path('', include(routers.urls)),
]