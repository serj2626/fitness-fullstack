from drf_spectacular.utils import extend_schema
from rest_framework import generics

from common.pagination import ListResultsSetPagination

from .models import Trainer, TrainerReviews
from .serializers import (
    TrainerListSerializer,
    TrainerDetailSerializer,
    TrainerReviewsSerializer,
    TrainerReviewsSerializer,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

TAG = "Тренеры"


@extend_schema(tags=[TAG], summary="Список отзывов о тренере")
@api_view(["GET"])
def get_all_comments_by_coach_id(request, coach_id):
    try:
        coach = Trainer.objects.get(pk=coach_id)
        reviews = coach.reviews.all()
        serializer = TrainerReviewsSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Trainer.DoesNotExist:
        return Response(
            data="Тренер не найден", status=status.HTTP_404_NOT_FOUND
        )


class TrainerReviewsCreateView(generics.CreateAPIView):
    serializer_class = TrainerReviewsSerializer
    queryset = TrainerReviews.objects.all()

    @extend_schema(tags=[TAG], summary="Добавить отзыв о тренере")
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class TrainerListView(generics.ListAPIView):
    serializer_class = TrainerListSerializer
    pagination_class = ListResultsSetPagination

    def get_queryset(self):
        return Trainer.objects.only(
            "id", "position", "first_name", "last_name", "experience", "avatar"
        )

    @extend_schema(tags=[TAG], summary="Список тренеров")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TrainerDetailView(generics.RetrieveAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerDetailSerializer

    @extend_schema(tags=[TAG], summary="Тренер")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
