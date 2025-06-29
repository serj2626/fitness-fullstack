from django.urls import path
from .views import (
    RegisterView,
    UserDetailView,
    UserListView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", CustomTokenVerifyView.as_view(), name="token_verify"),
    path("", UserListView.as_view(), name="user-list"),
    path("me/", UserDetailView.as_view(), name="user-detail"),
]
