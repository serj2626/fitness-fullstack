from django.contrib import admin

from common.admin_actions import get_admin_link

from .models import (
    Abonement,
    AbonementService,
    AbonementServiceAbonement,
    OrderAbonement,
)


@admin.register(AbonementService)
class AbonementServiceAdmin(admin.ModelAdmin):
    """Admin View for AbonementService"""

    list_display = (
        "name",
        "slug",
    )


class AbonementServiceAbonementInline(admin.TabularInline):
    model = AbonementServiceAbonement


@admin.register(Abonement)
class AbonementAdmin(admin.ModelAdmin):
    """Admin View for Abonement"""

    list_display = (
        "name",
        "slug",
        "order",
        "count_months",
        "price",
        "days_freezing",
        "is_popular",
    )

    fieldsets = (
        (
            "Данные абонемента",
            {
                "fields": (
                    ("name", "slug"),
                    ("count_months", "days_freezing"),
                    "price",
                    "order",
                    "content",
                )
            },
        ),
    )
    list_editable = ("order", "is_popular")
    readonly_fields = ("slug",)

    inlines = (AbonementServiceAbonementInline,)


@admin.register(OrderAbonement)
class OrderAbonementAdmin(admin.ModelAdmin):
    """Admin View for OrderAbonement"""

    list_display = (
        "order_by_time",
        "get_user_link",  # Ссылка на пользователя
        "get_abonement_link",  # Ссылка на абонемент
        "is_payed",
        "date_start",
        "date_end",
        "total_time",
        "created_at",
    )
    readonly_fields = ("date_end", "created_at")

    # Ссылка на пользователя
    @admin.display(description="Пользователь", ordering="user")
    def get_user_link(self, obj):
        return get_admin_link(obj, "user", "admin:users_user_change")

    # ✅ Ссылка на абонемент
    @admin.display(description="Абонемент", ordering="abonement")
    def get_abonement_link(self, obj):
        return get_admin_link(obj, "abonement", "admin:abonements_abonement_change")

    @admin.display(description="Заказ от")
    def order_by_time(self, obj):
        date = obj.created_at.strftime("%d.%m.%Y")
        return f"Заказ от {date}"

    @admin.display(description="Кол-во месяцев")
    def total_time(self, obj):
        return obj.abonement.count_months

    list_display_links = ("order_by_time",)
