from django.db import models
from common.models import BaseDate, BaseTitle


SOCIAL_ICON_TYPES = [
    ("vk", "Вконтакте"),
    ("telegram", "Телеграм"),
    ("whatsapp", "Ватсап"),
    ("linkedin", "Linkedin"),
]

CONTACTS_TYPE = [
    ("phone", "Телефон"),
    ("mail", "Почта"),
    ("address", "Адрес"),
    ("mode", "Режим работы"),
    ("latitude", "Широта"),
    ("longitude", "Долгота"),
]


class Feedback(BaseDate):
    """
    Обратная связь
    """

    name = models.CharField("Имя", max_length=255)
    phone = models.CharField("Телефон", max_length=255)
    agree = models.BooleanField("Согласие", default=False)
    verified = models.BooleanField("Проверен", default=False)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return f"Обратная связь от {self.name} от {self.created_at}"


class Footer(models.Model):
    site_name = models.CharField(
        max_length=100, default="AlfaSms", verbose_name="Название сайта"
    )
    copyright = models.CharField(
        "Копирайт", max_length=255, default="© 2025 DVFitness. All rights reserved."
    )

    def __str__(self):
        return f"Футер"

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футер"


class FooterLink(BaseTitle):
    """
    Модель ссылок для футера
    """

    link = models.CharField("Ссылка", max_length=255)
    footer = models.ForeignKey(
        Footer,
        on_delete=models.CASCADE,
        related_name="links",
        verbose_name="Футер",
    )

    def __str__(self):
        return f"Ссылка в футере {self.title}"

    class Meta:
        verbose_name = "Ссылка в футере"
        verbose_name_plural = "Ссылки в футере"


class FooterIcon(models.Model):
    """
    Модель иконок для футера
    """

    title = models.CharField(
        "Название", max_length=255, unique=True, choices=SOCIAL_ICON_TYPES
    )
    link = models.CharField("Ссылка", max_length=255)
    footer = models.ForeignKey(
        Footer,
        on_delete=models.CASCADE,
        related_name="icons",
        verbose_name="Футер",
    )

    def __str__(self):
        return f"Ссылка в футере {self.title}"

    class Meta:
        verbose_name = "Иконка в футере"
        verbose_name_plural = "Иконки в футере"


class Contact(models.Model):
    """
    Модель контактов
    """

    type = models.CharField(
        max_length=50,
        choices=CONTACTS_TYPE,
        default="phone",
        verbose_name="Тип",
        unique=True,
    )
    value = models.TextField(max_length=500, verbose_name="Значение")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"Контакт {self.get_type_display()}"
