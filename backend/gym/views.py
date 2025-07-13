from drf_spectacular.utils import extend_schema
from rest_framework import generics

from common.pagination import ListResultsSetPagination

from .models import FAQ, GymReviews, Post, Service
from .serializers import (
    FAQSerializer,
    GymReviewsSerializer,
    PostSerializer,
    ServiceSerializer,
)

TAG = "Тренажерный зал"


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"

    @extend_schema(tags=["Посты"], summary="Детальное отображение новости")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostLastView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")[:5]

    @extend_schema(tags=["Посты"], summary="Последние новости")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @extend_schema(tags=["Посты"], summary="Список новостей")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


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
