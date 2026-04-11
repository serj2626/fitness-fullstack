from django.contrib import admin

from products.models import Basket

from .models import CreateCodeSendEmail, User


class BasketTabularInline(admin.TabularInline):
    model = Basket
    extra = 0


class CreateCodeSendEmailInline(admin.TabularInline):
    model = CreateCodeSendEmail
    extra = 0
    max_num = 1
    fields = ("code", "get_expired")
    readonly_fields = ("get_expired",)  # ← Обязательно для методов

    def get_expired(self, obj):
        return obj.is_expired()

    get_expired.short_description = "Истек"
    get_expired.boolean = True


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
        "is_staff",
        "is_superuser",
        "is_active",
        "has_basket",
    )
    inlines = [BasketTabularInline, CreateCodeSendEmailInline]
    readonly_fields = ("password", "has_basket")  # ← Методы тоже сюда

    fields = (
        ("email", "phone"),
        "password",
        "last_login",
        (
            "is_active",
            "is_staff",
        ),
        "is_superuser",
    )

    def has_basket(self, obj):
        return "✅" if obj.basket.exists() else "❌"

    has_basket.short_description = "Корзина"
