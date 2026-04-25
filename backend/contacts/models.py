from datetime import date

from django.db import models

from common.mixins import AutoSlugMixin, TimeAgoModelMixin
from common.models import BaseContent, BaseDate, BaseDescription, BaseOrder

CONTACTS_TYPE = [
    ("city", "Город"),
    ("address", "Адрес"),
    ("email", "Почта"),
    ("phone", "Телефон"),
    ("other_phone", "Другой телефон"),
    ("mode", "Режим работы"),
    ("map", "Широта"),
    ("longitude", "Долгота"),
]

SOCIALS_TYPE = [
    ("vk", "VK"),
    ("tg", "TELEGRAM"),
    ("max", "MAX"),
    ("insta", "INSTAGRAM"),
    ("youtube", "YOUTUBE"),
    ("whatsapp", "WHATSAPP"),
]


class Policy(BaseContent):
    class Meta:
        verbose_name = "Политика конфиденциальности"
        verbose_name_plural = "Политика конфиденциальности"


class Terms(BaseContent):
    class Meta:
        verbose_name = "Пользовательское соглашение"
        verbose_name_plural = "Пользовательское соглашение"


class FeedBack(BaseDate, BaseDescription):
    """
    Модель обратной связи
    """

    name = models.CharField(
        "Имя",
        max_length=350,
    )
    phone = models.CharField("Телефон", max_length=255)
    is_verified = models.BooleanField("Проверен", default=False)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"


class Footer(models.Model):
    text = models.TextField("Текст")
    developer_name = models.CharField("Имя разработчика", max_length=255)
    developer_link = models.URLField("Ссылка разработчика")

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футер"

    def __str__(self):
        return f"Футер {self.id}"

    @property
    def copyright(self):
        """Возвращает текст копирайта с текущим годом"""
        current_year = date.today().year
        return f"© {current_year} Все права защищены."


class FAQ(BaseOrder):
    """
    Модель вопросов и ответов
    """

    question = models.TextField("Вопрос")
    answer = models.TextField(
        max_length=1000,
        verbose_name="Ответ",
        default="Здравствуйте",
        help_text="Максимум 1000 символов",
    )

    class Meta:
        verbose_name = "Вопрос и ответ"
        verbose_name_plural = "Вопросы и ответы"
        ordering = ["order", "question"]

    def __str__(self):
        return f"Вопрос {self.question}"


class Contact(models.Model):
    """
    Модель контактов
    """

    type = models.CharField(
        max_length=50, choices=CONTACTS_TYPE, verbose_name="Тип контакта"
    )
    value = models.CharField(max_length=255, verbose_name="Значение")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"Контакт {self.get_type_display()}"


class Social(models.Model):
    """
    Модель социальных сетей
    """

    type = models.CharField(
        max_length=50, choices=SOCIALS_TYPE, verbose_name="Тип контакта"
    )
    value = models.CharField(max_length=255, verbose_name="Значение")

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return f"Социальная сеть {self.get_type_display()}"


class Vacancy(TimeAgoModelMixin, BaseContent, BaseDate, BaseOrder, AutoSlugMixin):
    """
    Модель вакансий
    """

    title = models.TextField(
        "Название вакансии",
        max_length=300,
        help_text="Например: Мастер маникюра / педикюра",
        blank=False,
        unique=True,
    )
    slug = models.SlugField(
        "Слаг",
        max_length=300,
        blank=True,
        null=True,
        unique=True,
        help_text="Будет использован в ссылке на вакансию",
    )
    is_active = models.BooleanField(
        "Активна", default=False, help_text="Отображать ли вакансию на сайте"
    )

    meta_title = models.CharField(
        "Meta Title", max_length=255, blank=True, help_text="Не трогать"
    )
    meta_description = models.TextField(
        "Meta Description", blank=True, help_text="Не трогать"
    )

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = [
            "order",
        ]

    def __str__(self):
        return f"Вакансия {self.title}"
