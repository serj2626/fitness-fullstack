from drf_spectacular.utils import extend_schema

from common.pagination import ListResultsSetPagination
from .models import FAQ, GymReviews, Service
from .serializers import FAQSerializer, GymReviewsSerializer, ServiceSerializer
from rest_framework import generics

TAG = "Тренажерный зал"


class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    pagination_class = ListResultsSetPagination

    @extend_schema(tags=[TAG], summary="Список FAQ")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    @extend_schema(tags=[TAG], summary="Услуги")
    def get(self, request):
        return super().list(request)


class GymReviewsListView(generics.CreateAPIView):
    queryset = GymReviews.objects.all()
    serializer_class = GymReviewsSerializer

    @extend_schema(tags=[TAG], summary="Отзывы")
    def post(self, request):
        return super().create(request)
