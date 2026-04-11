from django.urls import path

from .views import (
    CreateCodeSendEmailView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    RegisterView,
    VerifyEmailView,
    get_info_user,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", CustomTokenVerifyView.as_view(), name="token_verify"),
    path("send-code/", CreateCodeSendEmailView.as_view(), name="verify_code"),
    path("verify-code/", VerifyEmailView.as_view(), name="verify_code"),
    path("info/", get_info_user, name="get_info_user"),
]
