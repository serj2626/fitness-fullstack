from django.contrib import admin

from common.mixins import AdminImagePreviewMixin

from .models import Coach, CoachReview, CoachService, OrderTraining, Service


@admin.register(CoachReview)
class CoachReviewAdmin(admin.ModelAdmin):
    """Admin View for CoachReview"""

    list_display = (
        "user",
        "coach",
        "rating",
        "get_text",
    )

    def get_text(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 0 else 'Отзыв без текста'
    get_text.short_description = "Текст отзыва"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin View for Service"""

    list_display = ("name", "slug")
    readonly_fields = ("slug",)


class CoachServiceInline(admin.TabularInline):
    model = CoachService
    extra = 1
    classes = ("collapse",)


class OrderTrainingInline(admin.TabularInline):
    model = OrderTraining
    extra = 1
    fields = ("service", "date_start", "date_end", "is_payed")
    classes = ("collapse",)


@admin.register(Coach)
class CoachAdmin(AdminImagePreviewMixin, admin.ModelAdmin):
    """Admin View for Coach"""

    image_field_name = "avatar"

    list_display = (
        "get_fullname",
        "get_all_categories",
        "email",
        "phone",
        "experience",
        "get_image",
    )
    save_on_top = True
    inlines = [CoachServiceInline, OrderTrainingInline]
    filter_horizontal = ("categories",)

    fieldsets = (
        (
            "Данные тренера",
            {
                "fields": (
                    ("first_name", "last_name"),
                    ("phone", "email"),
                    "avatar",
                    "experience",
                )
            },
        ),
        (
            "Категории",
            {
                "fields": ("categories",),
            },
        ),
    )

    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_all_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])

    get_all_categories.short_description = "Категории"
    get_fullname.short_description = "ФИО"


@admin.register(OrderTraining)
class OrderTrainingAdmin(admin.ModelAdmin):
    """Admin View for OrderTraining"""

    list_display = (
        "user",
        "coach",
        "service",
        "is_payed",
        "date_start",
        "date_end",
        "total_time",
        "created_at",
    )
    readonly_fields = ("date_end",)

    def total_time(self, obj):
        return f"{obj.service.time} мин."

    total_time.short_description = "Время"
