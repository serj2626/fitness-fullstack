from datetime import timedelta

from django.db import models
from django.utils import timezone

from categories.models import Category
from common.mixins import AutoSlugMixin, NameMixin, TimeAgoModelMixin
from common.models import BaseContent, BaseDate, BaseEmail, BaseID, BaseOrder
from common.upload import compress_image
from users.models import User


class Service(AutoSlugMixin, NameMixin):
    """
    Модель услуги
    """

    image = models.ImageField(
        "Изображение", upload_to="services/", blank=True, null=True
    )
    description = models.TextField("Описание", max_length=5000, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress_image(self.image, quality=80)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f"Услуга {self.name}"


class Coach(BaseID, BaseEmail, BaseContent, BaseOrder):
    """
    Модель тренера
    """

    first_name = models.CharField("Имя", max_length=255)
    last_name = models.CharField("Фамилия", max_length=255)
    phone = models.CharField("Телефон", max_length=255, blank=True, null=True)
    avatar = models.ImageField(
        "Изображение", upload_to="coaches/", blank=True, null=True
    )
    categories = models.ManyToManyField(Category, verbose_name="Категории")
    experience = models.PositiveSmallIntegerField(
        "Опыт работы", help_text="В годах", blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if self.avatar:
            self.avatar = compress_image(self.avatar)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    def __str__(self):
        return f"Тренер {self.first_name} {self.last_name}"


class CoachService(models.Model):
    """
    Модель связи тренеров и услуг
    """

    coach = models.ForeignKey(
        Coach, on_delete=models.CASCADE, verbose_name="Тренер", related_name="services"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, verbose_name="Услуга", related_name="coaches"
    )
    price = models.PositiveSmallIntegerField(
        "Цена", blank=True, null=True, help_text="Цена в рублях от ..."
    )
    time = models.PositiveSmallIntegerField(
        "Время",
        help_text="В минутах",
        choices=[(45, 45), (60, 60), (75, 75), (90, 90)],
    )

    class Meta:
        verbose_name = "Услуга тренера"
        verbose_name_plural = "Услуги тренеров"

    def __str__(self):
        return f"{self.coach.first_name} {self.coach.last_name} / {self.service.name} / {self.time} мин. / {self.price} руб."


class OrderTraining(BaseDate):
    """
    Модель бронирования тренировки
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="order_trainings",
    )

    coach = models.ForeignKey(
        Coach,
        on_delete=models.CASCADE,
        verbose_name="Тренер",
        related_name="order_trainings",
    )
    service = models.ForeignKey(
        CoachService,
        on_delete=models.CASCADE,
        verbose_name="Услуга",
        related_name="order_trainings",
    )
    is_payed = models.BooleanField("Оплачен", default=False)
    date_start = models.DateTimeField("Дата начала", blank=True, null=True)
    date_end = models.DateTimeField("Дата окончания", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.date_start:
            self.date_start = timezone.now().date()
        if not self.date_end:
            self.date_end = self.date_start + timedelta(minutes=self.service.time)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Бронирование тренировки"
        verbose_name_plural = "Бронирования тренировок"

    def __str__(self):
        return f"Бронирование тренировки {self.service.service.name}"


class CoachReview(BaseDate, TimeAgoModelMixin):
    """
    Модель отзыва о тренере
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="coach_reviews",
    )
    coach = models.ForeignKey(
        Coach,
        on_delete=models.CASCADE,
        verbose_name="Тренер",
        related_name="reviews",
    )
    rating = models.PositiveSmallIntegerField(
        "Рейтинг",
        help_text="От 1 до 5",
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
    )
    text = models.TextField("Комментарий", max_length=5000, blank=True, null=True)

    class Meta:
        verbose_name = "Отзыв о тренере"
        verbose_name_plural = "Отзывы о тренерах"

    def __str__(self):
        return f"Отзыв о тренере {self.coach.first_name} {self.coach.last_name} / Рейтинг: {self.rating}"
