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
    class Meta:
        model = Abonement
        fields = "__all__"
