from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView
from common.utils import get_cache_ttl
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import About, CookiePolicy, Offerta, Policy
from .serializers import (
    AboutSerializer,
    CookiePolicySerializer,
    OffertaSerializer,
    PolicySerializer,
)

TAG = "Юридическая информация"


@extend_schema(tags=[TAG], summary="О нас")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class AboutView(RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_object(self):
        return self.queryset.first()


@extend_schema(tags=[TAG], summary="Оферта")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class OffertaView(RetrieveAPIView):
    queryset = Offerta.objects.all()
    serializer_class = OffertaSerializer

    def get_object(self):
        return self.queryset.first()


@extend_schema(tags=[TAG], summary="Политика конфиденциальности")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class PolicyView(RetrieveAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

    def get_object(self):
        return self.queryset.first()


@extend_schema(tags=[TAG], summary="Политика cookie")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class CookiePolicyView(RetrieveAPIView):
    queryset = CookiePolicy.objects.all()
    serializer_class = CookiePolicySerializer

    def get_object(self):
        return self.queryset.first()
