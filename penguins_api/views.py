from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Penguin
from .serializers import PenguinSerializer
from .permissions import IsUserOrReadOnly


class PenguinList(ListCreateAPIView):
    queryset = Penguin.objects.all()
    serializer_class = PenguinSerializer

class PenguinDetail(RetrieveUpdateDestroyAPIView):
    queryset = Penguin.objects.all()
    serializer_class = PenguinSerializer
    permission_classes = IsUserOrReadOnly, IsAuthenticated
