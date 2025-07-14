from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.utils.text import slugify

from common.models import BaseDate, BaseID
from common.types import ABONEMENT_TYPES, SERVICES_TYPE

User = get_user_model()


class Abonement(models.Model):
    """Модель абонемента в фитнес-клуб"""

    title = models.CharField(
        "Название", max_length=100, choices=ABONEMENT_TYPES, default="basic"
    )
    description = models.TextField("Описание", null=True, blank=True)
    price = models.PositiveSmallIntegerField("Цена", null=True, blank=True)
    number_of_months = models.SmallIntegerField("Количество месяцев")
    is_popular = models.BooleanField("Популярный", default=False)
    sale = models.BooleanField("Акция", default=False)
    freeze_days = models.PositiveSmallIntegerField(
        "Заморозка дней", null=True, blank=True, default=0
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_current_discount(self):
        now = timezone.now()
        return self.discounts.filter(
            start_date__lte=now, end_date__gte=now, is_active=True
        ).first()

    @property
    def final_price(self):
        discount = self.get_current_discount()
        if discount:
            return self.price * (1 - discount.percent / 100)
        return self.price

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"
        ordering = ["price"]

    def __str__(self):
        return f"{self.get_title_display()} - {self.price}₽"


class AbonementService(models.Model):
    """
    Услуга абонемента
    """

    title = models.CharField("Название", max_length=100, choices=SERVICES_TYPE)
    abonement = models.ForeignKey(
        Abonement,
        on_delete=models.CASCADE,
        related_name="services",
        verbose_name="Абонемент",
    )

    class Meta:
        verbose_name = "Услуга абонемента"
        verbose_name_plural = "Услуги абонементов"
        unique_together = ("abonement", "title")

    def __str__(self):
        return f"{self.get_title_display()}"


class Discount(models.Model):
    """
    Скидка
    """

    abonement = models.ForeignKey(
        Abonement,
        on_delete=models.CASCADE,
        related_name="discounts",
        verbose_name="Абонемент",
    )
    percent = models.PositiveSmallIntegerField("Процент скидки")
    start_date = models.DateTimeField("Начало действия")
    end_date = models.DateTimeField("Конец действия")
    is_active = models.BooleanField("Активна", default=True)

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

    def __str__(self):
        return f"Скидка {self.percent}% на {self.abonement.title}"


class OrderAbonement(BaseID, BaseDate):
    """
    Забронировать абонемент
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="abonements",
        verbose_name="Клиент",
    )
    abonement = models.ForeignKey(
        Abonement,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Абонемент",
    )
    start = models.DateField("Начало абонемента")
    end = models.DateField("Конец абонемента", blank=True, null=True)
    status = models.BooleanField("Оплачен", default=False)
    active = models.BooleanField("Активен", default=False)

    def save(self, *args, **kwargs):
        if not self.end:
            count_days = self.abonement.number_of_months * 30
            self.end = self.start + timedelta(days=count_days)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Забронированный абонемент"
        verbose_name_plural = "Забронированные абонементы"

    def __str__(self):
        return f"Order - {self.abonement} - {self.user.email}"


class FreezeAbonement(BaseID):
    """
    Заморозить абонемент
    """

    my_abonement = models.ForeignKey(
        OrderAbonement,
        on_delete=models.CASCADE,
        related_name="freezes",
        verbose_name="Абонемент",
    )
    start = models.DateField("Начало заморозки")
    end = models.DateField("Конец заморозки")

    class Meta:
        verbose_name = "Замороженный абонемент"
        verbose_name_plural = "Замороженные абонементы"

    def clean(self):
        if self.start > self.end:
            raise ValidationError(
                "Дата начала заморозки должна быть раньше даты окончания"
            )
        if self.start < timezone.now().date():
            raise ValidationError("Нельзя заморозить абонемент в прошлом")
        if self.start == timezone.now().date():
            raise ValidationError("Нельзя заморозить абонемент на сегодня")
        if self.end < timezone.now().date():
            raise ValidationError("Нельзя заморозить абонемент в прошлом")

    def __str__(self):
        return f"Freeze - {self.abonement} - {self.start} - {self.end}"


class GymVisit(BaseID):
    """
    Модель визита в фитнес-клуб
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="gym_visits",
        verbose_name="Пользователь",
    )
    order_abonement = models.ForeignKey(
        OrderAbonement,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Абонемент",
        related_name="visits",
    )
    visit_start = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время начала визита",
    )
    visit_end = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name="Дата и время окончания визита",
    )

    class Meta:
        verbose_name = "Визит в фитнес-клуб"
        verbose_name_plural = "Визиты в фитнес-клуб"
        ordering = ["-visit_start"]

    def __str__(self):
        return f"{self.user.email} - {self.visit_start}"

    @property
    def total_time(self):
        """Возвращает продолжительность визита, если он завершен"""
        if not self.visit_end:
            return None
        return self.visit_end - self.visit_start

    def clean(self):
        """Проверка, что visit_end не раньше visit_start"""
        if self.visit_end and self.visit_end < self.visit_start:
            raise ValidationError(
                "Дата окончания не может быть раньше даты начала!"
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
