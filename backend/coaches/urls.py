from django.urls import path

from .views import (
    CoachDetailView,
    CoachListReviewView,
    CoachListView,
    CreateOrderTrainingView,
)

urlpatterns = [
    path("coaches/", CoachListView.as_view(), name="coach-list"),
    path("coaches/<str:id>/", CoachDetailView.as_view(), name="coach-detail"),
    path("reviews/", CoachListReviewView.as_view(), name="reviews-list"),
    path("order/", CreateOrderTrainingView.as_view(), name="create-order"),
]
