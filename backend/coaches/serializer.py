from rest_framework import serializers
from .models import Coach, CoachService
from categories.serializers import CategorySerializer


class CoachServiceSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="service.name", read_only=True)

    class Meta:
        model = CoachService
        fields = ("id", "title", "price", "time")


class CoachSerializer(serializers.ModelSerializer):
    services = CoachServiceSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

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
