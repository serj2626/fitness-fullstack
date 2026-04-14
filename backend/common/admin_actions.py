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


def get_admin_link(obj, field_name: str, admin_url_name: str, display_text: str = None):
    """
    Генерирует HTML-ссылку на объект в админке Django.

    :param obj: Экземпляр модели
    :param field_name: Имя ForeignKey поля (например, 'user' или 'abonement')
    :param admin_url_name: URL имя админки (например, 'admin:users_user_change')
    :param display_text: Текст ссылки. По умолчанию берётся str(объекта)
    :return: HTML-строка или "-"
    """
    related = getattr(obj, field_name, None)
    if not related:
        return "-"

    try:
        url = reverse(admin_url_name, args=[related.pk])
        text = display_text or str(related)
        return format_html('<a href="{}">{}</a>', url, text)
    except Exception:
        # Если URL неверный или объект битый, админка не должна падать
        return str(related)
