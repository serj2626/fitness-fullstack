from django.contrib import admin
from .models import Contact, Feedback, Footer, FooterIcon, FooterLink


class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1


class FooterIconInline(admin.TabularInline):
    model = FooterIcon
    extra = 1


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    """Admin View for Footer)"""

    list_display = ("site_name", "copyright")
    inlines = [FooterLinkInline, FooterIconInline]


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
