from rest_framework.serializers import ModelSerializer

from .models import Penguin


class PenguinSerializer(ModelSerializer):

    class Meta:
        model = Penguin
        fields = 'id', 'user', 'name', 'species', 'description'
