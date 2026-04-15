from .views import CoachListView
from django.urls import path

urlpatterns = [
    path("coaches/", CoachListView.as_view(), name="coach-list"),
]
