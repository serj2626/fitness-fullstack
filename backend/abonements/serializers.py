from rest_framework import serializers
from .models import Abonement, GymVisit, AbonementService


class AbonementServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbonementService
        fields = ("title",)

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
