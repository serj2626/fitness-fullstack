from .serializers import CategorySerializer
from .models import Category
from rest_framework import generics
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Categories"], responses=CategorySerializer)
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
