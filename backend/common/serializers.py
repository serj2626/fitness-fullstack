from rest_framework import serializers


class StatusResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    result = serializers.CharField()
