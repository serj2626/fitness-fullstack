from django.db import models
from common.models import BaseOrder, BaseContent, BaseDate
from common.mixins import AutoSlugMixin, TimeAgoModelMixin, NameMixin
from users.models import User
from django.utils import timezone


class Abonement(BaseOrder, BaseContent, AutoSlugMixin, NameMixin):
    """
    Модель абонемента
    """
    count_months = models.PositiveSmallIntegerField(
        "Количество месяцев", default=1)
    price = models.PositiveSmallIntegerField(
        "Цена", blank=True, null=True, help_text="Цена в рублях от ...")

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"

    def __str__(self):
        return f"Абонемент {self.name}"


class OrderAbonement(models.Model):
    """
    Модель заказа абонемента
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name='abonements')
    abonement = models.ForeignKey(
        Abonement, on_delete=models.CASCADE, verbose_name="Абонемент")
    date_start = models.DateField("Дата начала")
    date_end = models.DateField("Дата окончания")

    class Meta:
        verbose_name = "Заказ абонемента"
        verbose_name_plural = "Заказы абонементов"
