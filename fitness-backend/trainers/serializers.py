from rest_framework import serializers
from .models import Trainer, TrainerImage, TrainerRate, TrainerReviews, TrainingSession
from django.db.models import Avg


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
        fields = ("name", "email", "rating", "text", "verified", "time_age")

    def get_time_age(self, obj):
        return obj.time_age


class TrainerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerImage
        fields = ("id", "image")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["avatar"] = instance.image.url
        return representation


class TrainerSerializer(serializers.ModelSerializer):
    images = TrainerImageSerializer(many=True, read_only=True)
    position = serializers.SerializerMethodField()
    rates = TrainerRateSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Trainer
        fields = "__all__"

    def get_position(self, obj):
        return obj.get_position_display()

    def get_average_rating(self, obj):
        return obj.trainer_reviews.aggregate(avg=Avg("rating"))["avg"] or 0
