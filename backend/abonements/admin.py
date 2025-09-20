from django.contrib import admin

from common.admin import AdminLimitMixin, AdminShortDescriptionMixin

from .models import (
    Abonement,
    Discount,
    GymVisit,
    OrderAbonement,
)




@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """
    Админка для скидок
    """

    list_display = (
        "abonement",
        "percent",
        "start_date",
        "end_date",
        "is_active",
    )


@admin.register(Abonement)
class AbonementAdmin(
    AdminShortDescriptionMixin, AdminLimitMixin, admin.ModelAdmin
):
    """Админка для абонементов"""

    singleton_limit = 3

    list_display = (
        "title",
        "get_description",
        "price",
        "number_of_months",
        "slug",
        "is_popular",
    )
    filter_horizontal = ("services",)



@admin.register(OrderAbonement)
class OrderAbonementAdmin(AdminShortDescriptionMixin, admin.ModelAdmin):
    """Админка для забронированных абонементов"""

    list_display = (
        "user",
        "abonement",
        "start",
        "end",
        "status",
        "active",
    )


@admin.register(GymVisit)
class GymVisitAdmin(AdminShortDescriptionMixin, admin.ModelAdmin):
    """Админка для визитов в фитнес-клуб"""

    list_display = (
        "user",
        "visit_start",
        "visit_end",
        "total_time",
    )
