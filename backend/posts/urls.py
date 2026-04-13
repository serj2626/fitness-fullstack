from django.urls import path

from .views import PostDetailView, PostLastListView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("last/", PostLastListView.as_view(), name="post-last"),
    path(
        "<slug:slug>/", PostDetailView.as_view(), name="post-detail"
    ),  # Обратите внимание на slug
]
