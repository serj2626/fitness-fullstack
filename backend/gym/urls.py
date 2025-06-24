from django.urls import path
from .views import FAQListView, ServiceListView, GymReviewsListView


urlpatterns = [
    path("services/", ServiceListView.as_view(), name="services"),
    path("reviews/", GymReviewsListView.as_view(), name="reviews"),
        path("faq/", FAQListView.as_view(), name="faq-list"),
]
