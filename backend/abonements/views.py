from .models import Abonement, GymVisit
from .serializers import AbonementSerializer, GymVisitSerializer
from rest_framework import generics
from drf_spectacular.utils import extend_schema


TAG = "Абонементы"


class GymVisitListView(generics.ListAPIView):
    queryset = GymVisit.objects.all()
    serializer_class = GymVisitSerializer

    @extend_schema(tags=[TAG], summary="Список визитов в фитнес-клуб")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AbonementListView(generics.ListAPIView):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer

    @extend_schema(tags=[TAG], summary="Список абонементов")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
