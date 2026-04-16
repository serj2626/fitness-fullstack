from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import Category
from .serializers import CategorySerializer

TAG = "Категории"


@extend_schema(tags=[TAG], responses=CategorySerializer)
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
