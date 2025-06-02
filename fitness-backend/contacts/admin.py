from django.contrib import admin
from .models import Contact, Feedback, Footer


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    """Admin View for Footer)"""

    list_display = ("site_name", "copyright")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin View for Contact)"""

    list_display = ("type", "value")
    search_fields = ("type", "value")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Admin View for Feedback)"""

    list_display = (
        "name",
        "phone",
        "agree",
        "verified",
    )
    search_fields = ("name", "phone")
