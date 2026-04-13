from django.contrib import admin

from common.admin_actions import make_active, make_not_active
from common.mixins import AdminImagePreviewMixin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin, AdminImagePreviewMixin):
    """Admin View for Post"""

    list_display = (
        "title",
        "slug",
        "type",
        "get_image",
        "created_at",
        "is_active",
    )
    save_on_top = True
    list_editable = ("is_active", "type")
    fields = (
        "title",
        ("type", "slug"),
        "content",
        "is_active",
        ("image", "get_large_image"),
    )
    readonly_fields = ("slug", "get_large_image")
    actions = [make_active, make_not_active]
