from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Abonement, OrderAbonement


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
    list_editable = ("order",)
    readonly_fields = ("slug",)


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
    def get_user_link(self, obj):
        if obj.user:
            # Путь: admin:приложение_модель_change
            url = reverse("admin:users_user_change", args=[obj.user.id])
            return format_html('<a href="{}">{}</a>', url, obj.user)
        return "-"

    get_user_link.short_description = "Пользователь"
    get_user_link.admin_order_field = "user"

    # Ссылка на абонемент
    def get_abonement_link(self, obj):
        if obj.abonement:
            # Путь: admin:приложение_модель_change
            url = reverse("admin:abonements_abonement_change", args=[obj.abonement.id])
            return format_html('<a href="{}">{}</a>', url, obj.abonement)
        return "-"

    get_abonement_link.short_description = "Абонемент"
    get_abonement_link.admin_order_field = "abonement"

    def order_by_time(self, obj):
        date = obj.created_at.strftime("%d.%m.%Y")
        return f"Заказ от {date}"

    def total_time(self, obj):
        return obj.abonement.count_months

    order_by_time.short_description = "Заказ от"

    total_time.short_description = "Кол-во месяцев"
    list_display_links = ("order_by_time",)
