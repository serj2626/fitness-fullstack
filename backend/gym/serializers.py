from rest_framework import serializers

from .models import (
    FAQ,
    Advantage,
    Equipment,
    GymReviews,
    Post,
    Service,
    Schedule,
)
from django.utils.timesince import timesince


class ScheduleSerializer(serializers.ModelSerializer):
    service = serializers.CharField(
        source='service.get_type_display', read_only=True
    )
    trainer = serializers.SerializerMethodField()
    time_age = serializers.SerializerMethodField()
    # duration = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = (
            'trainer',
            'service',
            'date',
            'start',
            'end',
            # 'duration',
            'max_participants',
            'current_participants',
            'status',
            "time_age",
            "created_at",
            "updated_at",
        )

    def get_trainer(self, obj):
        return {
            "id": obj.trainer.id,
            "full_name": f"{obj.trainer.first_name} {obj.trainer.last_name}",
            "position": obj.trainer.get_position_display(),
        }

    def get_time_age(self, obj):
        return timesince(obj.date) + " назад"
    
    # def get_duration(self, obj):
    #     return obj.end - obj.start


class EquipmentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Equipment
        fields = "__all__"


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_category(self, obj):
        return obj.get_category_display()


class GymReviewsSerializer(serializers.ModelSerializer):
    time_age = serializers.SerializerMethodField()

    class Meta:
        model = GymReviews
        fields = (
            "first_name",
            "last_name",
            "email",
            "rating",
            "text",
            "verified",
            "time_age",
        )

    def get_time_age(self, obj):
        return obj.time_age


class ServiceSerializer(serializers.ModelSerializer):
    alt = serializers.SerializerMethodField()
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = (
            "id",
            "alt",
            "type",
            "slug",
            "avatar",
            "img_url",
        )

    def get_alt(self, obj):
        return str(obj.get_type_display())

    def get_img_url(self, obj):
        return str(obj.avatar.url)

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation["avatar"] = instance.avatar.url
    #     return representation


class FAQSerializer(serializers.ModelSerializer):
    """
    Сериализатор для FAQ
    """

    class Meta:
        model = FAQ
        fields = "__all__"
