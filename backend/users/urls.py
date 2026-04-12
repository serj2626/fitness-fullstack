from django.urls import path
from .views import (
    RegisterRequestView, RegisterVerifyView,
    LoginRequestView, LoginVerifyView,
    LogoutView, MeView,
    PasswordResetRequestView, PasswordResetVerifyView,
    ChangePasswordView,
)

urlpatterns = [
    # Регистрация
    path('auth/register/request/',
         RegisterRequestView.as_view(), name='register-request'),
    path('auth/register/verify/',
         RegisterVerifyView.as_view(), name='register-verify'),

    # Вход
    path('auth/login/request/', LoginRequestView.as_view(), name='login-request'),
    path('auth/login/verify/', LoginVerifyView.as_view(), name='login-verify'),

    # Выход
    path('auth/logout/', LogoutView.as_view(), name='logout'),

    # Профиль
    path('auth/me/', MeView.as_view(), name='me'),

    # Пароль
    path('auth/password/reset/request/',
         PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('auth/password/reset/verify/',
         PasswordResetVerifyView.as_view(), name='password-reset-verify'),
    path('auth/password/change/',
         ChangePasswordView.as_view(), name='password-change'),
]
