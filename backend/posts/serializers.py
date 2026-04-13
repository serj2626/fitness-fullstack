from rest_framework import serializers

from common.utils import RelativeOnlyImageField

from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    image = RelativeOnlyImageField()

    class Meta:
        model = Post
        fields = ("id", "title", "slug", "type", "image", "content", "created_at")


class PostLastListSerializer(serializers.ModelSerializer):
    image = RelativeOnlyImageField()

    class Meta:
        model = Post
        fields = ("id", "title", "slug", "type", "image", "created_at")


class PostDetailSerializer(serializers.ModelSerializer):
    image = RelativeOnlyImageField()

    class Meta:
        model = Post
        exclude = ("updated_at", "is_active")
