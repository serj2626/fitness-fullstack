from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, OpenApiResponse, extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from categories.models import Category

from .models import Coach, CoachReview, OrderTraining
from .serializer import (
    CoachReviewListSerializer,
    CoachSerializer,
    CreateOrderTrainingSerializer,
)

TAG = "Тренеры"
TAG_REVIEW = "Отзывы о тренерах"


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
        )
    ],
)
class CoachListReviewView(ListAPIView):
    serializer_class = CoachReviewListSerializer
    queryset = CoachReview.objects.all()

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

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.request.query_params.get("category")
        if category_slug:
            queryset = queryset.filter(categories__slug=category_slug)
        return queryset


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
