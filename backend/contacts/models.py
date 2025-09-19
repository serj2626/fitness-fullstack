from django.db import models

from common.models import BaseDate, BaseTitle

CONTACTS_TYPE = [
    ("phone", "Телефон"),
    ("mail", "Почта"),
    ("tg", "Telegram"),
    ("whatsapp", "WhatsApp"),
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
    subtitle = models.CharField(
        max_length=100, default="AlfaSms", verbose_name="Подзаголовок"
    )
    copyright = models.CharField(
        "Копирайт",
        max_length=255,
        default="© 2025 ИП Соколов. Все права защищены.",
    )
    developer_name = models.CharField(
        "Разработчик", max_length=100, blank=True, null=True
    )
    developer_link = models.URLField(
        "Ссылка на разработчика", max_length=100, blank=True, null=True
    )

    def __str__(self):
        return f"Футер"

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футер"


class Navigation(models.Model):
    """
    Модель ссылок для футера
    """

    footer = models.ForeignKey(
        Footer,
        on_delete=models.CASCADE,
        related_name="navigations",
        verbose_name="Футер",
    )
    title = models.CharField("Ссылка", max_length=255, unique=True)
    link = models.CharField("Значение ссылки", max_length=255)

    def __str__(self):
        return f"Ссылка в футере {self.title}"

    class Meta:
        verbose_name = "Ссылка в футере"
        verbose_name_plural = "Ссылки в футере"

    def __str__(self):
        return f"Контакт {self.title}"


class Contact(models.Model):
    """
    Модель контактов
    """

    footer = models.ForeignKey(
        Footer,
        on_delete=models.CASCADE,
        related_name="contacts",
        verbose_name="Футер",
    )
    type = models.CharField(
        max_length=50,
        choices=CONTACTS_TYPE,
        default="phone",
        verbose_name="Тип",
        unique=True,
    )
    value = models.CharField(max_length=500, verbose_name="Значение")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        unique_together = ("type", "value")

    def __str__(self):
        return f"Контакт {self.get_type_display()}"
