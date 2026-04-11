from rest_framework import serializers

from .models import FAQ, Contact, FeedBack, Footer, Policy, Terms, Vacancy


class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = ("content",)


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ("content",)


class FooterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Footer
        fields = [
            "id",
            "text",
            "developer_name",
            "developer_link",
            "copyright",
        ]


class FeedBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedBack
        fields = ("name", "description", "phone", "created_at")
        extra_kwargs = {
            "created_at": {"read_only": True},
        }


class SocialSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ("id", "title", "type", "value")

    def get_title(self, obj):
        return obj.get_type_display()


class ContactSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ("id", "title", "type", "value")

    def get_title(self, obj):
        return obj.get_type_display()


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ("id", "title", "slug", "content", "time", "created_at")


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        exclude = ["order"]
