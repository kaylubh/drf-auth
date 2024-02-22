from django.urls import path
from .views import PenguinList, PenguinDetail


urlpatterns = [
    path('', PenguinList.as_view(), name='penguin_list'),
    path('<int:pk>/', PenguinDetail.as_view(), name='penguin_detail'),
]
