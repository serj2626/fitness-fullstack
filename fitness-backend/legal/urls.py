from django.urls import path
from .views import CookiePolicyView, AboutView, OffertaView, PolicyView


urlpatterns = [
    path("cookie-policy/", CookiePolicyView.as_view(), name="cookie-policy"),
    path("about-company/", AboutView.as_view(), name="about-company"),
    path("offerta/", OffertaView.as_view(), name="offerta"),
    path("policy/", PolicyView.as_view(), name="policy"),
]
