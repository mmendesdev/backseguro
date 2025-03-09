from rest_framework import viewsets

from mente_segura.users.api.serializers import ForcaSegurancaSerializer, UserSerializer
from mente_segura.users.models import ForcaSeguranca, User


class ForcaSegurancaViewSet(viewsets.ModelViewSet):
    queryset = ForcaSeguranca.objects.all()
    serializer_class = ForcaSegurancaSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer_class = UserSerializer
