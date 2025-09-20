from rest_framework import serializers

from .models import Abonement, GymVisit


class GymVisitSerializer(serializers.ModelSerializer):
    total_time = serializers.SerializerMethodField()

    class Meta:
        model = GymVisit
        fields = "__all__"

    def get_total_time(self, obj):
        return obj.total_time


class AbonementSerializer(serializers.ModelSerializer):
    # title = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    class Meta:
        model = Abonement
        fields = "__all__"

    def get_services(self, obj):
        return list(map(lambda x: x.get_type_display(), obj.services.all()))

    # def get_title(self, obj):
    #     return obj.get_title_display()
