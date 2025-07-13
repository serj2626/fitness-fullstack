from rest_framework import serializers

from .models import Abonement, AbonementService, GymVisit


class AbonementServiceSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = AbonementService
        fields = ("title",)

    def get_title(self, obj):
        return obj.get_title_display()


class GymVisitSerializer(serializers.ModelSerializer):
    total_time = serializers.SerializerMethodField()

    class Meta:
        model = GymVisit
        fields = "__all__"

    def get_total_time(self, obj):
        return obj.total_time


class AbonementSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    services = AbonementServiceSerializer(many=True)

    class Meta:
        model = Abonement
        fields = "__all__"

    def get_title(self, obj):
        return obj.get_title_display()
