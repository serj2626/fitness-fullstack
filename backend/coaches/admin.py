from django.contrib import admin

from common.admin_actions import get_admin_link
from common.mixins import AdminImagePreviewMixin
from common.utils import get_review_text

from .models import (
    Coach,
    CoachReview,
    CoachService,
    OrderTraining,
    Service,
    CoachSocial,
)


class CoachSocialInline(admin.TabularInline):
    model = CoachSocial
    extra = 1
    classes = ("collapse",)


@admin.register(CoachReview)
class CoachReviewAdmin(admin.ModelAdmin):
    """Admin View for CoachReview"""

    list_display = ("user", "coach", "rating", "get_text", "created_at", "is_verified")

    @admin.display(description="Текст отзыва")
    def get_text(self, obj):
        return get_review_text(obj.text)


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
    fields = ("service", "date_start", "date_end", "is_paid")
    classes = ("collapse",)


@admin.register(Coach)
class CoachAdmin(AdminImagePreviewMixin, admin.ModelAdmin):
    """Admin View for Coach"""

    image_field_name = "avatar"

    list_display = (
        "id",
        "get_fullname",
        "get_all_categories",
        "email",
        "phone",
        "experience",
        "get_image",
    )
    save_on_top = True
    inlines = [CoachSocialInline, CoachServiceInline, OrderTrainingInline]
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

    @admin.display(description="ФИО")
    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    @admin.display(description="Категории")
    def get_all_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])


@admin.register(OrderTraining)
class OrderTrainingAdmin(admin.ModelAdmin):
    """Admin View for OrderTraining"""

    list_display = (
        "get_order",
        "get_user_link",
        "get_coach_link",
        "service",
        "date_start",
        "date_end",
        "total_time",
        "created_at",
        "is_paid",
    )
    readonly_fields = ("date_end",)

    @admin.display(description="№ Заказ")
    def get_order(self, obj):
        date = obj.created_at.strftime("%d.%m.%Y")
        return f"Заказ от {date}"

    @admin.display(description="Время")
    def total_time(self, obj):
        return f"{obj.service.time} мин."

    @admin.display(description="Пользователь", ordering="user")
    def get_user_link(self, obj):
        return get_admin_link(obj, "user", "admin:users_user_change")

    @admin.display(description="Тренер", ordering="user")
    def get_coach_link(self, obj):
        return get_admin_link(obj, "coach", "admin:coaches_coach_change")
