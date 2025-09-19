from django.contrib import admin

from .models import CONTACTS_TYPE, Contact, Feedback, Footer, Navigation


class NavigationInline(admin.TabularInline):
    model = Navigation
    extra = 1
    max_num = 2


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
    max_num = len(CONTACTS_TYPE)


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    """Admin View for Footer)"""

    list_display = ("site_name", "copyright")
    inlines = [
        NavigationInline,
        ContactInline,
    ]


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
