import logging

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import Throttled
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.mail import send_feedback_email

from .models import FAQ, Contact, Footer, Policy, Social, Terms, Vacancy
from .serializers import (
    ContactSerializer,
    FAQSerializer,
    FeedBackSerializer,
    FooterSerializer,
    PolicySerializer,
    SocialSerializer,
    TermsSerializer,
    VacancySerializer,
)
from .throttles import FeedbackThrottle

# Кэширование (раскомментировать когда Redis подключен):
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from common.utils import get_cache_ttl


logger = logging.getLogger(__name__)

TAG = "Контакты"


class PolicyApiView(APIView):

    @extend_schema(
        tags=[TAG],
        summary="Политика конфиденциальности",
        description="Политика конфиденциальности",
    )
    def get(self, request):
        policy = Policy.objects.first()
        serializer = PolicySerializer(policy)
        return Response(serializer.data)


class TermsApiView(APIView):

    @extend_schema(
        tags=[TAG],
        summary="Пользовательское соглашение",
        description="Пользовательское соглашение",
    )
    def get(self, request):
        terms = Terms.objects.first()
        serializer = TermsSerializer(terms)
        return Response(serializer.data)


class FeedbackCreateView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [FeedbackThrottle]

    def handle_exception(self, exc):
        if isinstance(exc, Throttled):
            wait = int(exc.wait or 60)
            return Response(
                {
                    "status": "error",
                    "msg": f"Слишком много запросов. Повторите через {wait} сек.",
                },
                status=status.HTTP_429_TOO_MANY_REQUESTS,
            )
        return super().handle_exception(exc)

    @extend_schema(
        tags=[TAG],
        summary="Отправить обратную связь",
        description="Отправить обратную связь (лимит: 2 запроса в минуту)",
        request=FeedBackSerializer,
    )
    def post(self, request):
        serializer = FeedBackSerializer(data=request.data)
        if serializer.is_valid():
            feedback = serializer.save()
            try:
                send_feedback_email(
                    name=feedback.name,
                    phone=feedback.phone,
                    message=feedback.description or "",
                )
            except Exception as e:
                logger.error(f"Ошибка отправки email: {e}")
            return Response(
                {"status": "success", "msg": "Обратная связь успешно создана"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"status": "error", "msg": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


# @method_decorator(cache_page(get_cache_ttl(10)), name="dispatch")
class FooterApiView(APIView):
    @extend_schema(
        tags=[TAG],
        summary="Подвал",
        description="Подвал",
        responses={
            200: FooterSerializer,
            404: OpenApiTypes.OBJECT,
        },
    )
    def get(self, request):
        footer = Footer.objects.first()

        if not footer:
            return Response(
                {"error": "Футер не найден", "status": 404},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = FooterSerializer(footer)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    tags=[TAG],
    summary="Контакты",
    description="Контакты",
)
# @method_decorator(cache_page(get_cache_ttl(10)), name="dispatch")
class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


@extend_schema(
    tags=[TAG],
    summary="Социальные сети",
    description="Социальные сети",
)
# @method_decorator(cache_page(get_cache_ttl(10)), name="dispatch")
class SocialListView(ListAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


# @method_decorator(cache_page(get_cache_ttl(5)), name="dispatch")
class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    @extend_schema(
        tags=[TAG],
        summary="Список вопросов и ответов",
        description="Список вопросов и ответов",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class VacancyListView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [AllowAny]

    @extend_schema(
        tags=[TAG],
        summary="Список вакансий",
        description="Список вакансий",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
