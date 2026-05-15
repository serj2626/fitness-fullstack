from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    RegisterSerializer,
    UserSerializer,
)

TAG = "Auth и пользователи"


# ---------------------------------------------------------------------------
# 1. РЕГИСТРАЦИЯ
# ---------------------------------------------------------------------------
@extend_schema(
    tags=["Auth"],
    summary="Регистрация нового пользователя",
    description=(
        "Создаёт аккаунт, автоматически выполняет вход и возвращает данные пользователя "
        "вместе с CSRF-токеном. Устанавливает HTTP-Only cookie `sessionid`."
    ),
    request=RegisterSerializer,
    responses={
        201: inline_serializer(
            name="RegisterResponse",
            fields={"user": UserSerializer, "csrfToken": str},
        ),
        400: OpenApiResponse(
            description="Ошибки валидации (занятый email, несовпадение паролей и т.д.)"
        ),
    },
    examples=[
        OpenApiExample(
            name="Успешная регистрация",
            value={
                "email": "user@example.com",
                "phone": "+79991234567",
                "password": "strongPass123",
                "password2": "strongPass123",
            },
            response_only=False,
        )
    ],
)
@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)  # Автоматический вход + установка cookie sessionid
        return Response(
            {
                "user": UserSerializer(user, context={"request": request}).data,
                "csrfToken": get_token(request),
            },
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------------------------------------------------------------------
# 2. ЛОГИН
# ---------------------------------------------------------------------------
@extend_schema(
    tags=["Auth"],
    summary="Вход в систему",
    description=(
        "Аутентифицирует пользователя по email и паролю. "
        "Устанавливает сессию (cookie `sessionid`) и возвращает CSRF-токен "
        "для защиты последующих mutating-запросов."
    ),
    request=inline_serializer(
        name="LoginRequest",
        fields={"email": str, "password": str},
    ),
    responses={
        200: inline_serializer(
            name="LoginResponse",
            fields={"user": UserSerializer, "csrfToken": str},
        ),
        400: OpenApiResponse(description="Неверный email или пароль"),
    },
    examples=[
        OpenApiExample(
            name="Вход",
            value={"email": "user@example.com", "password": "strongPass123"},
            response_only=False,
        )
    ],
)
@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(request, email=email, password=password)
    if user:
        login(request, user)
        return Response(
            {
                "user": UserSerializer(user, context={"request": request}).data,
                "csrfToken": get_token(request),
            }
        )
    return Response(
        {"error": "Неверный email или пароль"}, status=status.HTTP_400_BAD_REQUEST
    )


# ---------------------------------------------------------------------------
# 3. ЛОГАУТ
# ---------------------------------------------------------------------------
@extend_schema(
    tags=["Auth"],
    summary="Выход из системы",
    description="Завершает текущую сессию, удаляет cookie `sessionid` на сервере и в браузере. Требует авторизации.",
    auth=["Session"],
    responses={200: OpenApiResponse(description="Успешный выход из системы")},
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({"success": True})


# ---------------------------------------------------------------------------
# 4. ТЕКУЩИЙ ПОЛЬЗОВАТЕЛЬ (ME)
# ---------------------------------------------------------------------------
@extend_schema(
    tags=["Auth"],
    summary="Данные текущего пользователя",
    description=(
        "Возвращает профиль авторизованного пользователя, включая сгенерированные абсолютные URL аватара. "
        "Требует валидную сессию."
    ),
    auth=["Session"],
    responses={
        200: UserSerializer,
        401: OpenApiResponse(description="Пользователь не авторизован"),
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me_view(request):
    serializer = UserSerializer(request.user, context={"request": request})
    return Response(serializer.data)


# ---------------------------------------------------------------------------
# 5. ОБНОВЛЕНИЕ ПРОФИЛЯ
# ---------------------------------------------------------------------------
@extend_schema(
    tags=["Auth"],
    summary="Обновление профиля",
    description=(
        "Частичное обновление данных профиля (PATCH). Поддерживает изменение имени, телефона и загрузку аватара. "
        "Требует авторизации."
    ),
    auth=["Session"],
    request=inline_serializer(
        name="UpdateProfileRequest",
        fields={
            "first_name": str,
            "last_name": str,
            "phone": str,
            "avatar": "file",
        },
    ),
    responses={
        200: UserSerializer,
        400: OpenApiResponse(description="Ошибки валидации данных"),
        401: OpenApiResponse(description="Требуется авторизация"),
    },
    examples=[
        OpenApiExample(
            name="Обновление телефона и имени",
            value={"first_name": "Иван", "phone": "+79001112233"},
            response_only=False,
        )
    ],
)
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_profile_view(request):
    user = request.user
    serializer = UserSerializer(
        user, data=request.data, partial=True, context={"request": request}
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @extend_schema(tags=["Auth"])
# class RegisterRequestView(APIView):
#     """Запрос на регистрацию - отправка кода на email"""

#     permission_classes = [AllowAny]

#     @extend_schema(request=RegisterRequestSerializer)
#     def post(self, request):
#         serializer = RegisterRequestSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         # Создаем пользователя в неактивном состоянии
#         user = User.objects.create(
#             email=serializer.validated_data["email"],
#             phone=serializer.validated_data.get("phone"),
#             is_active=False,
#         )

#         # Создаем и отправляем код
#         ip_address = self.get_client_ip(request)
#         verification_code = VerificationCode.create_for_user(
#             user, code_type="register", ip_address=ip_address
#         )
#         verification_code.send_email()

#         return Response(
#             {"message": "Код подтверждения отправлен на email", "email": user.email},
#             status=status.HTTP_200_OK,
#         )

#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(",")[0]
#         else:
#             ip = request.META.get("REMOTE_ADDR")
#         return ip


# @extend_schema(tags=["Auth"])
# class RegisterVerifyView(APIView):
#     """Подтверждение регистрации - ввод кода и пароля"""

#     permission_classes = [AllowAny]

#     @extend_schema(request=RegisterVerifySerializer)
#     def post(self, request):
#         serializer = RegisterVerifySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()

#         # Автоматический вход после регистрации
#         login(request, user)

#         return Response(
#             {
#                 "message": "Регистрация успешна",
#                 "user": UserSerializer(user, context={"request": request}).data,
#             },
#             status=status.HTTP_200_OK,
#         )


# @extend_schema(tags=["Auth"])
# class LoginRequestView(APIView):
#     """Запрос на вход - отправка кода на email"""

#     permission_classes = [AllowAny]

#     @extend_schema(request=LoginRequestSerializer)
#     def post(self, request):
#         serializer = LoginRequestSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         try:
#             user = User.objects.get(email=serializer.validated_data["email"])

#             # Создаем и отправляем код
#             ip_address = self.get_client_ip(request)
#             verification_code = VerificationCode.create_for_user(
#                 user, code_type="login", ip_address=ip_address
#             )
#             verification_code.send_email()

#             return Response(
#                 {
#                     "message": "Код подтверждения отправлен на email",
#                     "email": user.email,
#                 },
#                 status=status.HTTP_200_OK,
#             )

#         except User.DoesNotExist:
#             # Не показываем существует ли пользователь (безопасность)
#             return Response(
#                 {"message": "Код подтверждения отправлен на email"},
#                 status=status.HTTP_200_OK,
#             )

#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(",")[0]
#         else:
#             ip = request.META.get("REMOTE_ADDR")
#         return ip


# @extend_schema(tags=["Auth"])
# class LoginVerifyView(APIView):
#     """Подтверждение входа - ввод кода"""

#     permission_classes = [AllowAny]

#     @extend_schema(request=LoginVerifySerializer)
#     def post(self, request):
#         serializer = LoginVerifySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()

#         # Вход через сессию
#         login(request, user)

#         return Response(
#             {
#                 "message": "Вход выполнен успешно",
#                 "user": UserSerializer(user, context={"request": request}).data,
#             },
#             status=status.HTTP_200_OK,
#         )


# @extend_schema(tags=["Auth"])
# class LogoutView(APIView):
#     """Выход из аккаунта"""

#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         logout(request)
#         return Response({"message": "Выход выполнен успешно"})


# @extend_schema(tags=["Auth"])
# class MeView(APIView):
#     """Получение данных текущего пользователя"""

#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user, context={"request": request})
#         return Response(serializer.data)

#     def patch(self, request):
#         serializer = UserSerializer(
#             request.user, data=request.data, partial=True, context={"request": request}
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# @extend_schema(tags=["Auth"])
# class PasswordResetRequestView(APIView):
#     """Запрос на сброс пароля"""

#     permission_classes = [AllowAny]

#     @extend_schema(request=PasswordResetRequestSerializer)
#     def post(self, request):
#         serializer = PasswordResetRequestSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         try:
#             user = User.objects.get(email=serializer.validated_data["email"])

#             ip_address = self.get_client_ip(request)
#             verification_code = VerificationCode.create_for_user(
#                 user, code_type="reset_password", ip_address=ip_address
#             )
#             verification_code.send_email()

#             return Response(
#                 {"message": "Код для сброса пароля отправлен на email"},
#                 status=status.HTTP_200_OK,
#             )

#         except User.DoesNotExist:
#             return Response(
#                 {"message": "Код для сброса пароля отправлен на email"},
#                 status=status.HTTP_200_OK,
#             )

#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(",")[0]
#         else:
#             ip = request.META.get("REMOTE_ADDR")
#         return ip


# @extend_schema(tags=["Auth"])
# class PasswordResetVerifyView(APIView):
#     """Подтверждение сброса пароля"""

#     permission_classes = [AllowAny]

#     @extend_schema(request=PasswordResetVerifySerializer)
#     def post(self, request):
#         serializer = PasswordResetVerifySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(
#             {"message": "Пароль успешно изменён"}, status=status.HTTP_200_OK
#         )


# @extend_schema(tags=["Auth"])
# class ChangePasswordView(APIView):
#     """Смена пароля для авторизованного пользователя"""

#     permission_classes = [IsAuthenticated]

#     @extend_schema(request=ChangePasswordSerializer)
#     def post(self, request):
#         serializer = ChangePasswordSerializer(
#             data=request.data, context={"request": request}
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(
#             {"message": "Пароль успешно изменён"}, status=status.HTTP_200_OK
#         )
