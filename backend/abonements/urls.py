from django.urls import path

from .views import AbonementListView, GymVisitListView

urlpatterns = [
    path("", AbonementListView.as_view(), name="abonements-list"),
    path(
        "gym-visit/all/", GymVisitListView.as_view(), name="gym-all-visit-list"
    ),
]
