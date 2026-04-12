from django.db import models
from common.models import BaseContent, BaseOrder, BaseEmail, BaseID
from common.mixins import AutoSlugMixin, NameMixin
from categories.models import Category


class Service(AutoSlugMixin, NameMixin):
    """
    Модель услуги
    """

    image = models.ImageField(
        "Изображение", upload_to="services/", blank=True, null=True)
    description = models.TextField(
        "Описание", max_length=5000, blank=True, null=True)

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        return f"Сервис {self.name}"


class Coach(BaseID, BaseEmail, BaseContent, BaseOrder, AutoSlugMixin):
    """
    Модель тренера
    """
    first_name = models.CharField("Имя", max_length=255)
    last_name = models.CharField("Фамилия", max_length=255)
    phone = models.CharField("Телефон", max_length=255, blank=True, null=True)
    avatar = models.ImageField(
        "Изображение", upload_to="coaches/", blank=True, null=True)
    categories = models.ManyToManyField(Category, verbose_name="Категории")
    experience = models.PositiveSmallIntegerField(
        "Опыт работы", help_text="В годах", blank=True, null=True
    )

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    def __str__(self):
        return f"Тренер {self.name}"


class CoachService(models.Model):
    """
    Модель связи тренеров и услуг
    """

    coach = models.ForeignKey(
        Coach, on_delete=models.CASCADE, verbose_name="Тренер", related_name="services")
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, verbose_name="Услуга", related_name="coaches")
    price = models.PositiveSmallIntegerField(
        "Цена", blank=True, null=True, help_text="Цена в рублях от ...")

    class Meta:
        verbose_name = "Связь тренера и услуги"
        verbose_name_plural = "Связи тренеров и услуг"

    def __str__(self):
        return f"Связь тренера {self.coach.name} и услуги {self.service.name}"