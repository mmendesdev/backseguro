from django.contrib.auth import get_user_model
from rest_framework import serializers

from mente_segura.users.models import ForcaSeguranca


class ForcaSegurancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForcaSeguranca
        fields = ["id", "nome", "descricao", "tipo"]


class UserSerializer(serializers.ModelSerializer):
    forca_seguranca = serializers.PrimaryKeyRelatedField(
        queryset=ForcaSeguranca.objects.all()
    )

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "name",
            "cpf",
            "email",
            "data_de_cadastro",
            "forca_seguranca",
        ]
        model = get_user_model()
        fields = [
            "id",
            "name",
            "cpf",
            "email",
            "data_de_cadastro",
            "forca_seguranca",
        ]
