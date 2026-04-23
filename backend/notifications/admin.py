from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin View for Notification"""

    list_display = (
        "user",
        "type",
        "content_type",
        "object_id",
        "content_object",
        "get_text",
        "is_read",
    )

    @admin.display(description="Текст уведомления")
    def get_text(self, obj):
        return str(obj.message)[:30] + "..." if obj.message else "нет текста"
