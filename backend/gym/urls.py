from django.urls import path
from .views import (
    FAQListView,
    ServiceListView,
    GymReviewsListView,
    PostLastView,
    PostListView,
)


urlpatterns = [
    path("services/", ServiceListView.as_view(), name="services"),
    path("reviews/", GymReviewsListView.as_view(), name="reviews"),
    path("faq/", FAQListView.as_view(), name="faq-list"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/last/", PostLastView.as_view(), name="post-last"),
]
