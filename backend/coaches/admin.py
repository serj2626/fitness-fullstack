from django.contrib import admin

from common.mixins import AdminImagePreviewMixin

from .models import Coach, CoachService, OrderTraining, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin View for Service"""

    list_display = ("name", "slug")


class CoachServiceInline(admin.TabularInline):
    model = CoachService
    extra = 1


class OrderTrainingInline(admin.TabularInline):
    model = OrderTraining
    extra = 1
    fields = ("service", "date_start", "date_end", "is_payed")


@admin.register(Coach)
class CoachAdmin(AdminImagePreviewMixin, admin.ModelAdmin):
    """Admin View for Coach"""

    list_display = (
        "first_name",
        "last_name",
        "phone",
        "avatar",
        "experience",
        "get_image",
    )
    inlines = [CoachServiceInline, OrderTrainingInline]
    filter_horizontal = ("categories",)

    fieldsets = (
        (
            "Даннеые тренера",
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
            {"fields": ("categories",)},
        ),
    )


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
    )
