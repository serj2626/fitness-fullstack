from rest_framework import serializers

from .models import Abonement, OrderAbonement


class CreateOrderAbonementSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderAbonement
        fields = (
            "user",
            "abonement",
            "date_start",
        )


class AbonementSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()

    class Meta:
        model = Abonement
        fields = (
            "id",
            "name",
            "slug",
            "content",
            "count_months",
            "days_freezing",
            "price",
            "services",
        )

    def get_services(self, obj):
        return {"services": [service.service.name for service in obj.services.all()]}
