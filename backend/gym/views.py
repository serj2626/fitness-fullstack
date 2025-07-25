from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework import generics

from common.pagination import ListResultsSetPagination

from .models import (
    FAQ,
    Advantage,
    Equipment,
    GymReviews,
    Post,
    Service,
    Schedule,
)
from .serializers import (
    AdvantageSerializer,
    EquipmentSerializer,
    FAQSerializer,
    GymReviewsSerializer,
    PostSerializer,
    ServiceSerializer,
    ScheduleSerializer,
)

TAG = "Тренажерный зал"


class ScheduleListView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    @method_decorator(cache_page(60 * 60 * 1))
    @extend_schema(tags=[TAG], summary="Расписание занятий зала")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EquipmentListView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    @method_decorator(cache_page(60 * 60 * 3))
    @extend_schema(tags=[TAG], summary="Оборудование")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AdvantageListView(generics.ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer

    @method_decorator(cache_page(60 * 60 * 3))
    @extend_schema(tags=[TAG], summary="Преимущества")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


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

    @method_decorator(cache_page(60 * 60 * 3))
    @extend_schema(tags=[TAG], summary="Услуги")
    def get(self, request):
        return super().list(request)


class GymReviewsListView(generics.CreateAPIView):
    queryset = GymReviews.objects.all()
    serializer_class = GymReviewsSerializer

    @extend_schema(tags=[TAG], summary="Отзывы")
    def post(self, request):
        return super().create(request)
