from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from common.utils import get_cache_ttl
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
TAG_POST = "Новости и Статьи"


@extend_schema(tags=[TAG], summary="Расписание занятий зала")
class ScheduleListView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


@extend_schema(tags=[TAG], summary="Оборудование")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class EquipmentListView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


@extend_schema(tags=[TAG], summary="Преимущества")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class AdvantageListView(generics.ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer


@extend_schema(tags=[TAG_POST], summary="Детальное отображение новости")
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"


@extend_schema(tags=[TAG_POST], summary="Последние новости")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class PostLastView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")[:5]


@extend_schema(tags=[TAG_POST], summary="Список новостей")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@extend_schema(tags=[TAG], summary="Список FAQ")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    pagination_class = ListResultsSetPagination


@extend_schema(tags=[TAG], summary="Услуги")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


@extend_schema(tags=[TAG], summary="Отзывы", description="Создание отзывов")
class GymReviewsListView(generics.CreateAPIView):
    queryset = GymReviews.objects.all()
    serializer_class = GymReviewsSerializer
