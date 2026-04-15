from .serializers import AbonementSerializer, CreateOrderAbonementSerializer
from .models import Abonement
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from drf_spectacular.utils import extend_schema

TAG = "Абонементы"


@extend_schema(
    summary="Получить все абонементы",
    description="Получить все абонементы",
    tags=[TAG],
)
class AbonementListAPIView(ListAPIView):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer


@extend_schema(
    summary="Создать заказ на абонемент",
    description="Создать заказ на абонемент",
    tags=[TAG],
)
class CreateOrderAbonementAPIView(CreateAPIView):
    queryset = Abonement.objects.all()
    serializer_class = CreateOrderAbonementSerializer
