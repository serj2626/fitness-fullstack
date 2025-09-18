from django.db.models import Avg
from rest_framework import serializers

from gym.serializers import ServiceSerializer

from .models import (
    Trainer,
    TrainerImage,
    TrainerRate,
    TrainerReviews,
    TrainerSocialNetwork,
    TrainingSession,
)


class TrainerSocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerSocialNetwork
        fields = ("type", "link")


class TrainerRateSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = TrainerRate
        fields = ("id", "title", "count_minutes", "price", "description")

    def get_title(self, obj):
        return obj.get_title_display()


class TrainingSessionSerializer(serializers.ModelSerializer):
    trainer_first_name = serializers.CharField(source="trainer.first_name")
    trainer_last_name = serializers.CharField(source="trainer.last_name")
    trainer_position = serializers.CharField(source="trainer.position")
    trainer_id = serializers.CharField(source="trainer.id")

    class Meta:
        model = TrainingSession
        fields = (
            "client",
            "rate",
            "start",
            "end",
            "is_booked",
            "trainer_first_name",
            "trainer_last_name",
            "trainer_position",
            "trainer_id",
        )


class TrainerReviewsSerializer(serializers.ModelSerializer):
    time_age = serializers.SerializerMethodField()

    class Meta:
        model = TrainerReviews
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "rating",
            "text",
            "verified",
            "time_age",
            "trainer",
        )
        extra_kwargs = {
            "time_age": {"read_only": True},
            "verified": {"read_only": True},
        }

    def get_time_age(self, obj):
        return obj.time_age


class TrainerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerImage
        fields = ("id", "image")


class TrainerListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка тренеров
    """

    position = serializers.SerializerMethodField()

    class Meta:
        model = Trainer
        fields = (
            "id",
            "position",
            "first_name",
            "last_name",
            "experience",
            "avatar",
        )

    def get_position(self, obj):
        return obj.get_position_display()


class TrainerDetailSerializer(serializers.ModelSerializer):
    images = TrainerImageSerializer(many=True, read_only=True)
    position = serializers.SerializerMethodField()
    rates = TrainerRateSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    socials = TrainerSocialNetworkSerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Trainer
        fields = "__all__"

    def get_position(self, obj):
        return obj.get_position_display()

    def get_average_rating(self, obj):
        return obj.reviews.aggregate(avg=Avg("rating"))["avg"] or 0

    def get_photo(self, obj):
        if obj.avatar:
            return {
                "url_path": obj.avatar.url,
                "name_path": obj.avatar.name,
                "alt": f"Фото тренера {obj.first_name} {obj.last_name}",
            }
        return None
