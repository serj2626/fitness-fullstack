from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView

from common.pagination import ListResultsSetPagination

from .models import Post
from .serializers import (
    PostDetailSerializer,
    PostLastListSerializer,
    PostListSerializer,
)

TAG_POST = "Посты"


@extend_schema(
    tags=[TAG_POST], summary="Последние посты", description="Последние посты"
)
class PostLastListView(ListAPIView):
    queryset = Post.objects.filter(is_active=True).order_by("-created_at")[:5]
    serializer_class = PostLastListSerializer


@extend_schema(
    tags=[TAG_POST],
    summary="Список постов",
    description="Список постов",
    parameters=[
        OpenApiParameter(
            name="type",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Тип поста",
            enum=["article", "news"],
        )
    ],
)
class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = ListResultsSetPagination

    def get_queryset(self):
        type = self.request.query_params.get("type")
        queryset = Post.objects.filter(is_active=True).order_by("-created_at")
        if type:
            return queryset.filter(type=type)

        return queryset


@extend_schema(tags=[TAG_POST], summary="Пост", description="Пост")
class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = "slug"

    def get_object(self):
        return Post.objects.filter(is_active=True).get(slug=self.kwargs["slug"])
