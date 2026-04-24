from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
)
from django.db.models import Avg, Count, Q
from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from categories.models import Category
from common.pagination import ListResultsSetPagination

from .models import Coach, CoachReview, OrderTraining
from .serializer import (
    CoachLastSerializer,
    CoachReviewListSerializer,
    CoachSerializer,
    CreateOrderTrainingSerializer,
    CreateReviewByCoachSerializer,
)

TAG = "Тренеры"
TAG_REVIEW = "Отзывы о тренерах"


@extend_schema(
    tags=[TAG_REVIEW],
    summary="Создать отзыв о тренере",
    description="Этот эндпоинт позволяет создать отзыв о тренере."
    "coach d64cbfbc-9331-4ea7-9e3b-aa115d5f87bb \n"
    "user 	daf2a854-62ff-404c-aa29-c6b29b8eb073",
    request=CreateReviewByCoachSerializer,
    responses={
        200: CreateReviewByCoachSerializer,
        400: OpenApiResponse(description="Невалидные данные"),
        500: OpenApiResponse(description="Внутренняя ошибка сервера"),
    },
    examples=[
        OpenApiExample(
            name="Успешный отзыв",
            value={
                "user": "daf2a854-62ff-404c-aa29-c6b29b8eb073",
                "coach": "d64cbfbc-9331-4ea7-9e3b-aa115d5f87bb",
                "rating": 5,
                "text": "Профессионал своего дела!",
            },
            request_only=True,
        ),
        OpenApiExample(
            name="Отзыв с минимальным рейтингом",
            value={
                "user": "daf2a854-62ff-404c-aa29-c6b29b8eb073",
                "coach": "d64cbfbc-9331-4ea7-9e3b-aa115d5f87bb",
                "rating": 1,
                "text": "Не оправдал ожиданий.",
            },
            request_only=True,
        ),
    ],
)
class CreateReviewByCoachView(CreateAPIView):
    serializer_class = CreateReviewByCoachSerializer
    queryset = CoachReview.objects.all()


@extend_schema(
    tags=[TAG_REVIEW],
    summary="Получить список отзывов о тренерах",
    description="Этот эндпоинт возвращает список всех отзывов о тренерах.",
    responses={
        200: CoachReviewListSerializer(many=True),
        500: OpenApiResponse(description="Внутренняя ошибка сервера"),
    },
    parameters=[
        OpenApiParameter(
            name="id",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            required=False,
            description="ID тренера",
            enum=Coach.objects.values_list("id", flat=True),
        ),
        OpenApiParameter(
            name="ordering",
            location=OpenApiParameter.QUERY,
            type=OpenApiTypes.STR,
            description="ЗАНЧЕНИЕ СОРТИРОВКИ",
            enum=["created_at", "-created_at", "rating", "-rating"],
        ),
    ],
)
class CoachListReviewView(ListAPIView):
    serializer_class = CoachReviewListSerializer
    queryset = CoachReview.objects.all()
    pagination_class = ListResultsSetPagination

    # 🔥 Включаем фильтры и сортировку
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    ordering_fields = [
        "created_at",
        "rating",
    ]
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = super().get_queryset()
        coach_id = self.request.query_params.get("id")
        if coach_id:
            queryset = queryset.filter(coach_id=coach_id)
        return queryset


@extend_schema(
    tags=[TAG],
    summary="Получить список тренеров",
    description="Этот эндпоинт возвращает список всех тренеров с их услугами.",
    responses={
        200: CoachSerializer(many=True),
        500: OpenApiResponse(description="Внутренняя ошибка сервера"),
    },
    parameters=[
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            required=False,
            enum=Category.objects.values_list("slug", flat=True),
        )
    ],
)
class CoachListView(ListAPIView):
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()
    pagination_class = ListResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.request.query_params.get("category")
        if category_slug:
            queryset = queryset.filter(categories__slug=category_slug)
        return queryset


@extend_schema(
    tags=[TAG],
    summary="Получить список последних тренеров",
    description="Этот эндпоинт возвращает список последних тренеров.",
    responses={
        200: CoachLastSerializer(many=True),
        500: OpenApiResponse(description="Внутренняя ошибка сервера"),
    },
)
class CoachListLastView(ListAPIView):
    serializer_class = CoachLastSerializer
    queryset = Coach.objects.all()[:5]


@extend_schema(
    tags=[TAG],
    summary="Получить информацию о тренере",
    description="Этот эндпоинт возвращает информацию о конкретном тренере.",
    parameters=[
        OpenApiParameter(
            name="id",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.PATH,
            required=True,
            enum=Coach.objects.values_list("id", flat=True),
        )
    ],
    responses={
        200: CoachSerializer(),
        404: OpenApiResponse(description="Тренер не найден"),
        500: OpenApiResponse(description="Внутренняя ошибка сервера"),
    },
)
class CoachDetailView(RetrieveAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Coach.objects.annotate(
            average_rating=Avg(
                'reviews__rating',
                filter=Q(reviews__is_verified=False)
            ),
            reviews_count=Count(
                'reviews',
                filter=Q(reviews__is_verified=False)
            )
        )


@extend_schema(
    tags=[TAG],
    summary="Создать заказ на тренировку",
    description="Этот эндпоинт позволяет создать заказ на тренировку с конкретным тренером и услугой.",
    request=CreateOrderTrainingSerializer,
    responses={
        201: OpenApiResponse(description="Заказ успешно создан"),
        400: OpenApiResponse(description="Неверные данные запроса"),
        500: OpenApiResponse(description="Внутренняя ошибка сервера"),
    },
)
class CreateOrderTrainingView(CreateAPIView):
    serializer_class = CreateOrderTrainingSerializer
    queryset = OrderTraining.objects.all()
