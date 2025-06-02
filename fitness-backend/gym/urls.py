from django.urls import path
from .views import ServiceListView, GymReviewsListView


urlpatterns = [
    path("services/", ServiceListView.as_view(), name="services"),
    path("reviews/", GymReviewsListView.as_view(), name="reviews"),
]
