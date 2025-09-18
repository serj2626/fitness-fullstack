from drf_spectacular.utils import extend_schema
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Abonement, GymVisit
from .serializers import AbonementSerializer, GymVisitSerializer
from common.utils import get_cache_ttl

TAG = "Абонементы"


class GymVisitListView(generics.ListAPIView):
    queryset = GymVisit.objects.all()
    serializer_class = GymVisitSerializer

    @extend_schema(tags=[TAG], summary="Список визитов в фитнес-клуб")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@extend_schema(tags=[TAG], summary="Список абонементов")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class AbonementListView(generics.ListAPIView):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer
