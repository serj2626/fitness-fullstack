from rest_framework import serializers
from .models import Feedback, Contact, Footer, FooterLink, FooterIcon


class FooterLinkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для ссылок футера
    """

    class Meta:
        model = FooterLink
        fields = ("title", "link")


class FooterIconSerializer(serializers.ModelSerializer):
    """
    Сериализатор для иконок футера
    """

    class Meta:
        model = FooterIcon
        fields = ("title", "link")


class FooterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для футера
    """

    links = FooterLinkSerializer(many=True)
    icons = FooterIconSerializer(many=True)

    class Meta:
        model = Footer
        fields = ("site_name", "copyright", "links", "icons")


class ContactSerializer(serializers.ModelSerializer):
    """
    Сериализатор для контактов
    """

    second_type = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ("type", "second_type", "value")

    def get_second_type(self, instance):
        return instance.get_type_display()


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обратной связи
    """

    class Meta:
        model = Feedback
        fields = "__all__"
