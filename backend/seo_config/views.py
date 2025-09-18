from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView
from common.utils import get_cache_ttl
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from .models import SEO
from .serializers import SEOSerializer

TAG = "Настройки SEO и Конфигурация"


@extend_schema(tags=[TAG], summary="Получение SEO")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class SEOView(RetrieveAPIView):
    queryset = SEO.objects.all()
    serializer_class = SEOSerializer
    lookup_field = "slug"


@extend_schema(tags=[TAG], summary="Получение списка SEO")
class SEOListView(ListAPIView):
    queryset = SEO.objects.all()
    serializer_class = SEOSerializer
