from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, UserProfileQuestionnaire, VerificationCode


@admin.register(UserProfileQuestionnaire)
class UserProfileQuestionnaireAdmin(admin.ModelAdmin):
    """Admin View for UserProfileQuestionnaire"""

    list_display = ("id", "user")


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        "id",
        "email",
        "phone",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "created_at",
    ]
    list_filter = ["is_active", "is_staff", "created_at"]
    search_fields = ["email", "phone", "first_name", "last_name"]
    ordering = ["-created_at"]
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (None, {"fields": ("email", "phone", "password")}),
        ("Личная информация", {"fields": ("first_name", "last_name", "avatar")}),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Даты", {"fields": ("created_at", "updated_at")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "phone",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "user",
        "code_type",
        "is_used",
        "is_expired",
        "created_at",
        "expires_at",
    ]
    list_filter = ["code_type", "is_used", "created_at"]
    search_fields = ["code", "user__email"]
    readonly_fields = ["code", "is_expired"]

    def is_expired(self, obj):
        return obj.is_expired()

    is_expired.boolean = True
