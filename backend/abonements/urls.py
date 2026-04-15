from django.urls import path
from .views import AbonementListAPIView, CreateOrderAbonementAPIView

urlpatterns = [
    path("", AbonementListAPIView.as_view(), name="abonement-list"),
    path(
        "order/", CreateOrderAbonementAPIView.as_view(), name="create-order-abonement"
    ),
]
