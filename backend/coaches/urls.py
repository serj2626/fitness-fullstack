from django.urls import path

from .views import (
    CoachDetailView,
    CoachListReviewView,
    CoachListView,
    CreateOrderTrainingView,
    CreateReviewByCoachView,
)

urlpatterns = [
    path("", CoachListView.as_view(), name="coach-list"),
    path("reviews/", CoachListReviewView.as_view(), name="reviews-list"),
    path("reviews/create/", CreateReviewByCoachView.as_view(), name="create-review"),
    path("<str:id>/", CoachDetailView.as_view(), name="coach-detail"),
    path("order/", CreateOrderTrainingView.as_view(), name="create-order"),
]
