from django.contrib import admin
from django.utils.html import format_html, mark_safe

from common.admin import (
    AdminImagePreviewMixin,
    AdminShortDescriptionMixin,
    AdminLimitMixin,
)
from common.types import SERVICES_TYPE

from .models import (
    FAQ,
    Advantage,
    Equipment,
    GymReviews,
    Post,
    Service,
    Schedule,
    RecordOnSchedule,
)


@admin.register(RecordOnSchedule)
class AdminRecordOnSchedule(admin.ModelAdmin):
    '''Admin View for RecordOnSchedule'''

    list_display = ('user', "schedule")


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    '''Admin View for Schedule'''

    list_display = (
        'trainer',
        'service',
        'date',
        'start',
        'end',
        'status',
    )

    fields = (
        ('trainer', 'service'),
        ('start', 'end'),
        'date',
        'status',
        "avatar_preview",
    )

    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        if obj.trainer.avatar and hasattr(obj.trainer.avatar, "url"):
            return format_html(
                f'<img src="{obj.trainer.avatar.url}" width="260" height="260" style="object-fit:contain;" />'
            )
        return "—"

    avatar_preview.short_description = "Аватар тренера"


@admin.register(Equipment)
class InlineAdmin(AdminImagePreviewMixin, admin.ModelAdmin):
    '''Admin View for Equipment'''

    list_display = ('title', "get_image")


@admin.register(Advantage)
class AdvantageAdmin(
    AdminLimitMixin, AdminShortDescriptionMixin, admin.ModelAdmin
):
    list_display = ("title", "icon_preview", "alt", "get_description")
    readonly_fields = ("icon_preview",)
    singleton_limit = 4

    def icon_preview(self, obj):
        if obj.icon and obj.icon.name.endswith(".svg"):
            return format_html(
                f'<img src="{obj.icon.url}" width="32" height="32" style="object-fit:contain;" />'
            )
        return "—"

    icon_preview.short_description = "Иконка"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Админка постов"""

    list_display = (
        "title",
        "category",
        "image",
        "is_published",
        "slug",
    )


@admin.register(FAQ)
class FAQAdmin(AdminLimitMixin, admin.ModelAdmin):
    """
    Админка вопросов и ответов
    """

    singleton_limit = 15
    list_display = ("question", "answer")


@admin.register(GymReviews)
class GymReviewsAdmin(admin.ModelAdmin):
    """Админка отзывов"""

    list_display = (
        "first_name",
        "last_name",
        "email",
        "rating",
        "get_text",
        "verified",
    )

    def get_text(self, obj):
        return f"{(str(obj.text))[0:26]}..."

    get_text.short_description = "Текст"


@admin.register(Service)
class ServiceAdmin(AdminLimitMixin, admin.ModelAdmin):
    """
    Админка услуг
    """

    singleton_limit = len(SERVICES_TYPE)
    list_display = ("type", "slug", "get_image")

    def get_image(self, obj):
        if obj.avatar and hasattr(obj.avatar, "url"):
            return mark_safe(
                f'<img src="{obj.avatar.url}" style="border-radius: 50%;" width="70" height="70">'
            )
        return "Нет изображения"

    get_image.short_description = "Фото"
