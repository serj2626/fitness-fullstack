from django.urls import path

from .views import (
    TrainerDetailView,
    TrainerListView,
    TrainerReviewsCreateView,
    get_all_comments_by_coach_id,
)

urlpatterns = [
    path("trainers/", TrainerListView.as_view(), name="trainers-list"),
    path(
        "trainers/<uuid:pk>/",
        TrainerDetailView.as_view(),
        name="trainers-detail",
    ),
    path(
        "trainers/<uuid:coach_id>/reviews/",
        get_all_comments_by_coach_id,
        name="trainer-reviews-list",
    ),
    path(
        "trainers/<coach_id>/reviews/create/",
        TrainerReviewsCreateView.as_view(),
        name="trainer-reviews-create",
    ),
]
