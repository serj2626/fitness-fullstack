from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import User
from .serializers import RegisterSerializer, UserDetailSerializer, UserInfoSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.permissions import IsAuthenticated

TAG = "Аутентификация и Пользователи"


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer

    @extend_schema(tags=[TAG], summary="Список пользователей")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=[TAG], summary="Текущий пользователь")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return self.request.user


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    @extend_schema(tags=[TAG], summary="Регистрация пользователя")
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Пользователь успешно зарегистрирован"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=[TAG],
    summary="Получение JWT токена",
    description="Возвращает access и refresh токены по email и паролю.",
    responses={
        200: OpenApiResponse(
            response={"access": "string", "refresh": "string"},
            description="Успешная аутентификация",
        )
    },
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(
    tags=[TAG],
    summary="Обновление JWT токена",
    description="Обновляет access токен по действующему refresh токену.",
    responses={
        200: OpenApiResponse(
            response={"access": "string"}, description="Новый access токен"
        )
    },
)
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(tags=[TAG], summary="Проверка токена")
class CustomTokenVerifyView(TokenVerifyView):
    pass
