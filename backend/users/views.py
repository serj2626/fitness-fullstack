from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .serialziers import (
    SendCodeSerializer,
    UserInfoSerializer,
    UserRegisterSerializer,
    VerifyCodeSerializer,
)
from .utils import create_verification_code

TAG = "Пользователи"
TAG_AUTH = "Авторизация, аутентификация и регистрация"


@extend_schema_view(
    post=extend_schema(
        tags=[TAG_AUTH],
        summary="Получение JWT-токенов",
        description="Принимает email и пароль, возвращает access и refresh токены.",
    )
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema_view(
    post=extend_schema(
        tags=[TAG_AUTH],
        summary="Обновление access-токена",
        description="Принимает refresh-токен, возвращает новый access-токен.",
    )
)
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema_view(
    post=extend_schema(
        tags=[TAG_AUTH],
        summary="Проверка токена",
        description="Проверяет валидность переданного токена (access или refresh).",
    )
)
class CustomTokenVerifyView(TokenVerifyView):
    pass


@extend_schema(tags=[TAG], summary="Получение информации о текущем пользователе")
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_info_user(request):
    user = request.user
    serializer = UserInfoSerializer(user)
    return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        tags=[TAG_AUTH],
        summary="Регистрация пользователя",
        request=UserRegisterSerializer,
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # is_active=False

            try:
                create_verification_code(user)  # ← Вызов утилиты
            except Exception as e:
                print(f"Ошибка отправки письма: {e}")

            return Response(
                {
                    "msg": "Пользователь зарегистрирован. Проверьте почту.",
                    "status": "success",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"errors": serializer.errors, "status": "error"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class CreateCodeSendEmailView(APIView):
    @extend_schema(
        tags=[TAG_AUTH],
        summary="Высылает код подтверждения на почту",
        request=SendCodeSerializer,
    )
    def post(self, request):
        serializer = SendCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "msg": "На вашу почту отправлен код подтверждения",
                    "status": "success",
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=[TAG_AUTH],
        summary="Подтверждение email кодом",
        request=VerifyCodeSerializer,
    )
    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)

        if serializer.is_valid():
            code_obj = serializer.validated_data["code_obj"]
            user = code_obj.user  # ← Получаем пользователя из кода

            # Активируем пользователя
            user.is_active = True
            user.save()

            # Помечаем код как использованный
            code_obj.is_used = True
            code_obj.save()

            return Response(
                {
                    "msg": "Email подтвержден. Теперь вы можете войти.",
                    "status": "success",
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {"errors": serializer.errors, "status": "error"},
            status=status.HTTP_400_BAD_REQUEST,
        )
