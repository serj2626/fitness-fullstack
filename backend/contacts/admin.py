from django.contrib import admin

from common.admin_actions import (
    make_active,
    make_is_verified,
    make_not_active,
    make_not_is_verified,
)
from common.mixins import MaxObjectsMixin
from common.utils import get_review_text
from .models import FAQ, Contact, FeedBack, Footer, Policy, Social, Terms, Vacancy


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    """Admin View for Policy"""

    list_display = ("get_info",)

    def get_info(self, obj):
        return "Политика конфиденциальности"

    get_info.short_description = "Информация"

    def has_add_permission(self, request):
        if Policy.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    """Admin View for Terms"""

    list_display = ("get_info",)

    def get_info(self, obj):
        return "Пользовательское соглашение"

    get_info.short_description = "Информация"

    def has_add_permission(self, request):
        if Terms.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    """Admin View for Footer"""

    list_display = ("get_text", "developer_name", "developer_link", "copyright")

    def has_add_permission(self, request):
        if Footer.objects.exists():
            return False
        return super().has_add_permission(request)

    def get_text(self, obj):
        return str(obj.text)[:20] + "........." if obj.text else "Нет текста"

    get_text.short_description = "Текст"


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    """Admin View for FeedBack"""

    list_display = ("name", "phone", "get_text", "is_verified", "created_at")
    actions = [make_is_verified, make_not_is_verified]

    @admin.display(description="Текст отзыва")
    def get_text(self, obj):
        return get_review_text(obj.description)


@admin.register(FAQ)
class FAQAdmin(MaxObjectsMixin, admin.ModelAdmin):
    """Admin View for FAQ"""

    max_objects = 15

    list_display = (
        "generate_question",
        "generate_answer",
        "order",
    )

    list_editable = ("order",)

    def generate_question(self, obj):
        if obj.question:
            return str(obj.question)[:30] + "..."
        else:
            return "Нет вопроса"

    generate_question.short_description = "Вопрос"

    def generate_answer(self, obj):
        if obj.answer:
            return str(obj.answer)[:30] + "..."
        else:
            return "Нет ответа"

    generate_answer.short_description = "Ответ"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin View for Contact"""

    list_display = (
        "type",
        "value",
    )


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    """Admin View for Social"""

    list_display = (
        "type",
        "value",
    )


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """Admin View for Vacancy"""

    list_display = (
        "title",
        "slug",
        "created_at",
        "updated_at",
        "order",
        "is_active",
    )

    actions = [make_active, make_not_active]

    list_editable = ("is_active", "order")
    save_on_top = True
    fields = (
        "title",
        "content",
        "is_active",
        "order",
    )
