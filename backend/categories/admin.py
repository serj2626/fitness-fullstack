from django.contrib import admin

from common.mixins import AdminImagePreviewMixin

from .models import Category


@admin.register(Category)
class CategoryAdmin(AdminImagePreviewMixin, admin.ModelAdmin):
    """Admin View for Category"""

    list_display = ("name", "order", "slug", "get_image")
    fields = ("name", "slug", "image", "order")
    list_editable = ("order",)
    readonly_fields = ("slug",)
