from rest_framework import serializers

from .models import FAQ, GymReviews, Post, Service, Advantage


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
        fields = ("first_name", "last_name", "email", "rating", "text", "verified", "time_age")

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
