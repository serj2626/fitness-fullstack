from django.contrib import admin

from common.mixins import AdminImagePreviewMixin
from .models import Trainer, TrainerImage, TrainerReviews, TrainingSession, TrainerRate
from django.utils.html import mark_safe


@admin.register(TrainerRate)
class TrainerRateAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели TrainerRate
    """

    list_display = (
        "id",
        "trainer",
        "count_minutes",
        "price",
        "description",
    )
    list_display = (
        "trainer",
    )


@admin.register(TrainerReviews)
class TrainerReviewsAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели TrainerReviews
    """

    list_display = ("trainer", "name", "email", "rating", "get_text", "verified")
    list_filter = ("trainer", "rating")
    search_fields = ("trainer", "rating")

    def get_text(self, obj):
        return f"{(str(obj.text))[0:26]}..."

    get_text.short_description = "Текст"


class TrainerRateInline(admin.TabularInline):
    model = TrainerRate
    extra = 1


class TrainerImageInline(admin.TabularInline):
    model = TrainerImage
    extra = 1
    fields = ("image",)

    # def get_image(self, obj):
    #     if obj.image and hasattr(obj.image, "url"):
    #         return mark_safe(
    #             f'<img src="{obj.image.url}" style="border-radius: 50%;" width="50" height="50">'
    #         )
    #     return "Нет изображения"

    # get_image.short_description = "Фото"


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели Trainer
    """

    inlines = [TrainerImageInline, TrainerRateInline]

    list_display = (
        "id",
        "position",
        "first_name",
        "last_name",
        "email",
        "phone",
        "get_avatar",
    )
    list_filter = ("position",)
    list_per_page = 5
    save_on_top = True
    search_fields = ("first_name", "last_name", "email", "phone")

    def get_avatar(self, obj):
        if obj.avatar and hasattr(obj.avatar, "url"):
            return mark_safe(
                f'<img src="{obj.avatar.url}" style="border-radius: 50%;" width="50" height="50">'
            )
        return "Нет изображения"

    get_avatar.short_description = "Фото"


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели TrainingSession
    """

    list_display = (
        "trainer",
        "client",
        "rate",
        "start",
        "end",
        "is_booked",
    )
