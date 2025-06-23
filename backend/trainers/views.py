from common.pagination import ListResultsSetPagination
from .serializers import TrainerListSerializer, TrainerSerializer
from rest_framework import generics
from .models import Trainer
from drf_spectacular.utils import extend_schema

TAG = "Тренеры"


class TrainerListView(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerListSerializer
    pagination_class = ListResultsSetPagination

    @extend_schema(tags=[TAG], summary="Список тренеров")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TrainerDetailView(generics.RetrieveAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    @extend_schema(tags=[TAG], summary="Тренер")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
