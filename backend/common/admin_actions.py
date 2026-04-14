from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


@admin.action(description="Сделать выбранные записи активными")
def make_active(modeladmin, request, queryset):
    # queryset — это те записи, которые ты выбрал
    updated = queryset.update(is_active=True)
    modeladmin.message_user(request, f"Обновлено записей: {updated}")


@admin.action(description="Сделать выбранные записи не активными")
def make_not_active(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Сделать выбранные записи проверенными")
def make_is_verified(modeladmin, request, queryset):
    # queryset — это те записи, которые ты выбрал
    updated = queryset.update(is_verified=True)
    modeladmin.message_user(request, f"Обновлено записей: {updated}")


@admin.action(description="Сделать выбранные записи не проверенными")
def make_not_is_verified(modeladmin, request, queryset):
    queryset.update(is_verified=False)


@admin.action(description="Сделать выбранные товары новинками")
def make_new(modeladmin, request, queryset):
    # queryset — это те записи, которые ты выбрал
    updated = queryset.update(is_new=True)
    modeladmin.message_user(request, f"Обновлено записей: {updated}")


@admin.action(description="Сделать выбранные товары не новинками")
def make_not_new(modeladmin, request, queryset):
    queryset.update(is_new=False)


def get_abonement_link(self, obj):
    if obj.abonement:
        # Путь: admin:приложение_модель_change
        url = reverse("admin:abonements_abonement_change", args=[obj.abonement.id])
        return format_html('<a href="{}">{}</a>', url, obj.abonement)
    return "-"
