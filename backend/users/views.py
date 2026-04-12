from rest_framework import status, generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import login, logout, get_user_model
from django.core.mail import send_mail
from django.conf import settings
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import VerificationCode
from .serializers import (
    UserSerializer,
    RegisterRequestSerializer, RegisterVerifySerializer,
    LoginRequestSerializer, LoginVerifySerializer,
    PasswordResetRequestSerializer, PasswordResetVerifySerializer,
    ChangePasswordSerializer,
)

User = get_user_model()


@extend_schema(tags=['Auth'])
class RegisterRequestView(APIView):
    """Запрос на регистрацию - отправка кода на email"""
    permission_classes = [AllowAny]
    
    @extend_schema(request=RegisterRequestSerializer)
    def post(self, request):
        serializer = RegisterRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Создаем пользователя в неактивном состоянии
        user = User.objects.create(
            email=serializer.validated_data['email'],
            phone=serializer.validated_data.get('phone'),
            is_active=False
        )
        
        # Создаем и отправляем код
        ip_address = self.get_client_ip(request)
        verification_code = VerificationCode.create_for_user(
            user, code_type='register', ip_address=ip_address
        )
        verification_code.send_email()
        
        return Response({
            'message': 'Код подтверждения отправлен на email',
            'email': user.email
        }, status=status.HTTP_200_OK)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


@extend_schema(tags=['Auth'])
class RegisterVerifyView(APIView):
    """Подтверждение регистрации - ввод кода и пароля"""
    permission_classes = [AllowAny]
    
    @extend_schema(request=RegisterVerifySerializer)
    def post(self, request):
        serializer = RegisterVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Автоматический вход после регистрации
        login(request, user)
        
        return Response({
            'message': 'Регистрация успешна',
            'user': UserSerializer(user, context={'request': request}).data
        }, status=status.HTTP_200_OK)


@extend_schema(tags=['Auth'])
class LoginRequestView(APIView):
    """Запрос на вход - отправка кода на email"""
    permission_classes = [AllowAny]
    
    @extend_schema(request=LoginRequestSerializer)
    def post(self, request):
        serializer = LoginRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            user = User.objects.get(email=serializer.validated_data['email'])
            
            # Создаем и отправляем код
            ip_address = self.get_client_ip(request)
            verification_code = VerificationCode.create_for_user(
                user, code_type='login', ip_address=ip_address
            )
            verification_code.send_email()
            
            return Response({
                'message': 'Код подтверждения отправлен на email',
                'email': user.email
            }, status=status.HTTP_200_OK)
            
        except User.DoesNotExist:
            # Не показываем существует ли пользователь (безопасность)
            return Response({
                'message': 'Код подтверждения отправлен на email'
            }, status=status.HTTP_200_OK)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


@extend_schema(tags=['Auth'])
class LoginVerifyView(APIView):
    """Подтверждение входа - ввод кода"""
    permission_classes = [AllowAny]
    
    @extend_schema(request=LoginVerifySerializer)
    def post(self, request):
        serializer = LoginVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Вход через сессию
        login(request, user)
        
        return Response({
            'message': 'Вход выполнен успешно',
            'user': UserSerializer(user, context={'request': request}).data
        }, status=status.HTTP_200_OK)


@extend_schema(tags=['Auth'])
class LogoutView(APIView):
    """Выход из аккаунта"""
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response({'message': 'Выход выполнен успешно'})


@extend_schema(tags=['Auth'])
class MeView(APIView):
    """Получение данных текущего пользователя"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)
    
    def patch(self, request):
        serializer = UserSerializer(
            request.user, 
            data=request.data, 
            partial=True,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@extend_schema(tags=['Auth'])
class PasswordResetRequestView(APIView):
    """Запрос на сброс пароля"""
    permission_classes = [AllowAny]
    
    @extend_schema(request=PasswordResetRequestSerializer)
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            user = User.objects.get(email=serializer.validated_data['email'])
            
            ip_address = self.get_client_ip(request)
            verification_code = VerificationCode.create_for_user(
                user, code_type='reset_password', ip_address=ip_address
            )
            verification_code.send_email()
            
            return Response({
                'message': 'Код для сброса пароля отправлен на email'
            }, status=status.HTTP_200_OK)
            
        except User.DoesNotExist:
            return Response({
                'message': 'Код для сброса пароля отправлен на email'
            }, status=status.HTTP_200_OK)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


@extend_schema(tags=['Auth'])
class PasswordResetVerifyView(APIView):
    """Подтверждение сброса пароля"""
    permission_classes = [AllowAny]
    
    @extend_schema(request=PasswordResetVerifySerializer)
    def post(self, request):
        serializer = PasswordResetVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'message': 'Пароль успешно изменён'
        }, status=status.HTTP_200_OK)


@extend_schema(tags=['Auth'])
class ChangePasswordView(APIView):
    """Смена пароля для авторизованного пользователя"""
    permission_classes = [IsAuthenticated]
    
    @extend_schema(request=ChangePasswordSerializer)
    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, 
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'message': 'Пароль успешно изменён'
        }, status=status.HTTP_200_OK)