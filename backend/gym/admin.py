from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.html import format_html
from .models import FAQ, GymReviews, Post, Service, Advantage, Equipment
from common.admin import AdminShortDescriptionMixin, AdminImagePreviewMixin


@admin.register(Equipment)
class InlineAdmin(AdminImagePreviewMixin, admin.ModelAdmin):
    '''Admin View for Equipment'''

    list_display = ('title', "get_image")


@admin.register(Advantage)
class AdvantageAdmin(AdminShortDescriptionMixin, admin.ModelAdmin):
    list_display = ("title", "icon_preview", "alt", "get_description")
    readonly_fields = ("icon_preview",)

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
class FAQAdmin(admin.ModelAdmin):
    """
    Админка вопросов и ответов
    """

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
class ServiceAdmin(admin.ModelAdmin):
    """
    Админка услуг
    """

    list_display = ("type", "slug", "get_image")

    def get_image(self, obj):
        if obj.avatar and hasattr(obj.avatar, "url"):
            return mark_safe(
                f'<img src="{obj.avatar.url}" style="border-radius: 50%;" width="70" height="70">'
            )
        return "Нет изображения"

    get_image.short_description = "Фото"
