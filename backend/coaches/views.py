from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializer import CoachSerializer
from .models import Coach
from drf_spectacular.utils import extend_schema, OpenApiResponse


@extend_schema(
    summary="Получить список тренеров",
    description="Этот эндпоинт возвращает список всех тренеров с их услугами.",
    responses={
        200: CoachSerializer(many=True),
        500: OpenApiResponse(description="Внутренняя ошибка сервера"),
    },
)
class CoachListView(ListAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
