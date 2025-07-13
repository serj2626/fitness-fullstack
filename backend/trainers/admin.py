from django.contrib import admin

from common.admin import AdminImagePreviewMixin

from .models import (
    Trainer,
    TrainerImage,
    TrainerRate,
    TrainerReviews,
    TrainerSocialNetwork,
    TrainingSession,
)


class TrainerSocialNetworkInline(admin.TabularInline):
    model = TrainerSocialNetwork
    extra = 1
    max_num = 4


class TrainingSessionInline(admin.TabularInline):
    model = TrainingSession
    extra = 1


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
    list_display = ("trainer",)


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
    max_num = 3


class TrainerImageInline(admin.TabularInline):
    model = TrainerImage
    extra = 1
    fields = ("image", "alt")


@admin.register(Trainer)
class TrainerAdmin(AdminImagePreviewMixin, admin.ModelAdmin):
    """
    Админ-панель для модели Trainer
    """

    image_field_name = "avatar"
    image_preview_width = 80
    image_preview_height = 80

    inlines = [
        TrainerImageInline,
        TrainerRateInline,
        TrainingSessionInline,
        TrainerSocialNetworkInline,
    ]

    list_display = (
        "id",
        "position",
        "get_full_name",
        "email",
        "phone",
        "get_image",
    )
    fields = (
        ("first_name", "last_name"),
        ("email", "phone"),
        (
            "position",
            "experience",
        ),
        "education",
        (
            "avatar",
            "get_image",
        ),
        "keywords",
        "content",
        "services",
    )
    list_filter = ("position",)
    list_per_page = 5
    save_on_top = True
    search_fields = ("first_name", "last_name", "email", "phone")

    filter_horizontal = ("services",)
    readonly_fields = ("get_image",)

    def get_full_name(self, obj):
        if obj.first_name and obj.last_name:
            return f"{obj.first_name} {obj.last_name}"
        return obj.email

    get_full_name.short_description = "Имя"


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
