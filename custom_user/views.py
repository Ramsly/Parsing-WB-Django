from rest_framework import viewsets

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet для модели CustomUser."""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
