from rest_framework import serializers

from .models import Contact, Feedback, Footer, Navigation


class ContactSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(
        source="get_type_display", read_only=True
    )

    class Meta:
        model = Contact
        fields = ("type", "type_display", "value")


class NavigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navigation
        fields = ("title", "link")


class FooterSerializer(serializers.ModelSerializer):
    navigations = NavigationSerializer(many=True, read_only=True)
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Footer
        fields = (
            "site_name",
            "subtitle",
            "copyright",
            "developer_name",
            "developer_link",
            "navigations",
            "contacts",
        )


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обратной связи
    """

    class Meta:
        model = Feedback
        fields = "__all__"
