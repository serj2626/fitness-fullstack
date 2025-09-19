from drf_spectacular.utils import extend_schema
from rest_framework import generics, response, status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from common.mixins import BaseSectionViewMixin
from common.utils import get_cache_ttl

from .models import Contact, Feedback, Footer
from .serializers import (
    ContactSerializer,
    FeedbackSerializer,
    FooterSerializer,
)

TAG = "Контакты"


@extend_schema(tags=[TAG], summary="Футер")
@method_decorator(cache_page(get_cache_ttl()), name="dispatch")
class FooterView(BaseSectionViewMixin):
    model = Footer
    serializer_class = FooterSerializer

    def get_queryset(self):
        return Footer.objects.all().prefetch_related("navigations", "contacts")


@extend_schema(tags=[TAG], summary="Список контактов")
@method_decorator(cache_page(get_cache_ttl()), name="dispatch")
class ContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class FeedbackView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    @extend_schema(tags=[TAG], summary="Отправить обратную связь")
    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return response.Response(
            {"msg": "Форма успешно отправлена", "status": "success"},
            status=status.HTTP_201_CREATED,
        )
