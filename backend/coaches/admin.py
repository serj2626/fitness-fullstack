from django.contrib import admin

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
    fields = ('service', "date_start", "date_end", "is_payed")


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    """Admin View for Coach"""

    list_display = (
        "first_name",
        "last_name",
        "phone",
        "avatar",
        "experience",
    )
    inlines = [CoachServiceInline, OrderTrainingInline]


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
