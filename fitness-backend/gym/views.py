from drf_spectacular.utils import extend_schema
from .models import GymReviews, Service
from .serializers import GymReviewsSerializer, ServiceSerializer
from rest_framework import generics

TAG = "Тренажерный зал"


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
