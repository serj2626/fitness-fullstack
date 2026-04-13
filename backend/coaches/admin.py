from django.contrib import admin

from common.mixins import AdminImagePreviewMixin

from .models import Coach, CoachService, OrderTraining, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin View for Service"""

    list_display = ("name", "slug")
    readonly_fields = ("slug",)


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
    )
