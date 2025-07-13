from django.contrib import admin
from django.utils.html import mark_safe

from .models import FAQ, GymReviews, Post, Service


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

    list_display = ("name", "email", "rating", "get_text", "verified")

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
