from django.urls import path
from .views import TrainerListView, TrainerDetailView


urlpatterns = [
    path("trainers/", TrainerListView.as_view(), name="trainers-list"),
    path("trainers/<uuid:pk>/", TrainerDetailView.as_view(), name="trainers-detail"),
]
