from rest_framework import serializers

from common.utils import RelativeOnlyImageField
from .models import Coach, CoachService, CoachReview, OrderTraining
from categories.serializers import CategorySerializer


class CreateOrderTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTraining
        fields = (
            "user",
            "coach",
            "service",
            "date_start",
        )


class CoachReviewListSerializer(serializers.ModelSerializer):
    time_ago = serializers.CharField(source="time", read_only=True)
    user = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = CoachReview
        fields = ("id", "user", "coach", "rating", "text", "time_ago")


class CoachReviewSerializer(serializers.ModelSerializer):
    time_ago = serializers.CharField(source="time", read_only=True)
    user = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = CoachReview
        fields = ("id", "user", "rating", "text", "time_ago")


class CoachServiceSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="service.name", read_only=True)

    class Meta:
        model = CoachService
        fields = ("id", "title", "price", "time")


class CoachSerializer(serializers.ModelSerializer):
    services = CoachServiceSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    avatar = RelativeOnlyImageField(read_only=True)

    class Meta:
        model = Coach
        fields = (
            "id",
            "first_name",
            "avatar",
            "last_name",
            "experience",
            "email",
            "phone",
            "categories",
            "services",
        )
