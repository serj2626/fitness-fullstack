from datetime import timedelta

from django.db import models
from django.utils import timezone

from common.mixins import AutoSlugMixin, NameMixin
from common.models import BaseContent, BaseDate, BaseOrder
from users.models import User


class AbonementService(NameMixin, AutoSlugMixin):
    """
    Модель услуги абонемента
    """

    class Meta:
        verbose_name = "Услуга абонемента"
        verbose_name_plural = "Услуги абонемента"

    def __str__(self):
        return f"Услуга {self.name}"

class Abonement(BaseOrder, BaseContent, NameMixin, AutoSlugMixin):
    """
    Модель абонемента
    """

    count_months = models.PositiveSmallIntegerField("Количество месяцев", default=1)
    price = models.PositiveSmallIntegerField(
        "Цена", blank=True, null=True, help_text="Цена в рублях от ..."
    )
    days_freezing = models.PositiveSmallIntegerField("Дни заморозки", default=0)

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"

    def __str__(self):
        return f"Абонемент {self.name} от {self.price} руб. / {self.count_months} мес."


class AbonementServiceAbonement(models.Model):
    abonement = models.ForeignKey(
        Abonement,
        on_delete=models.CASCADE,
        verbose_name="Абонемент",
        related_name="services",
    )
    service = models.ForeignKey(
        AbonementService,
        on_delete=models.CASCADE,
        verbose_name="Услуга",
        related_name="abonements",
    )

    class Meta:
        verbose_name = "Услуга абонемента"
        verbose_name_plural = "Услуги абонемента"

    def __str__(self):
        return f"Услуга {self.service.name} в абонементе {self.abonement.name}"


class OrderAbonement(BaseDate):
    """
    Модель заказа абонемента
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="order_abonements",
    )
    abonement = models.ForeignKey(
        Abonement,
        on_delete=models.CASCADE,
        verbose_name="Абонемент",
        related_name="order_abonements",
    )
    is_payed = models.BooleanField("Оплачен", default=False)
    date_start = models.DateField("Дата начала", blank=True, null=True)
    date_end = models.DateField("Дата окончания", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.date_start:
            self.date_start = timezone.now().date()
        if not self.date_end:
            self.date_end = self.date_start + timedelta(
                days=30 * self.abonement.count_months
            )
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Заказ абонемента"
        verbose_name_plural = "Заказы абонементов"

    def __str__(self):
        return f"Заказ абонемента {self.abonement.name} от {self.user.email}"
