from .serializers import CategorySerializer
from .models import Category
from rest_framework import generics
from drf_spectacular.utils import extend_schema


TAG = 'Категории'


@extend_schema(tags=[TAG], responses=CategorySerializer)
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
