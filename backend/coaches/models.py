from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from contacts.models import SOCIALS_TYPE
from categories.models import Category
from common.mixins import AutoSlugMixin, NameMixin, TimeAgoModelMixin
from common.models import (
    BaseContent,
    BaseDate,
    BaseDateRange,
    BaseEmail,
    BaseID,
    BaseOrder,
)
from common.upload import compress_image
from users.models import User


class OrderStatus(models.TextChoices):
    PENDING_PAYMENT = "pending_payment", "Ожидает оплаты"
    PAID = "paid", "Оплата подтверждена"
    PENDING = "pending", "Ожидает подтверждения"
    CONFIRMED = "confirmed", "Подтверждено"
    CANCELLED = "cancelled", "Отменено"
    COMPLETED = "completed", "Завершено"


class WorkoutStatus(models.TextChoices):
    SCHEDULED = "scheduled", "Запланирована"
    COMPLETED = "completed", "Проведена"
    CANCELLED = "cancelled", "Отменена"
    NO_SHOW = "no_show", "Клиент не пришёл"


class WorkoutType(models.TextChoices):
    PERSONAL = "personal", "Персональная тренировка"
    NO_TRAINER = "no_trainer", "Тренировка без тренера"


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


class CoachSocial(models.Model):
    """
    Модель социальных сетей тренера
    """

    coach = models.ForeignKey(
        Coach, on_delete=models.CASCADE, verbose_name="Тренер", related_name="socials"
    )
    social = models.CharField("Социальная сеть", max_length=255, choices=SOCIALS_TYPE)
    link = models.URLField("Ссылка", max_length=255)

    class Meta:
        verbose_name = "Социальная сеть тренера"
        verbose_name_plural = "Социальные сети тренеров"

    def __str__(self):
        return f"{self.coach.first_name} {self.coach.last_name} / {self.social}"


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


class OrderTraining(BaseDate, BaseDateRange):
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
    is_paid = models.BooleanField("Оплачен", default=False)
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        verbose_name="Статус",
    )

    def save(self, *args, **kwargs):
        if self.date_start and not self.date_end:
            self.date_end = self.date_start + timedelta(minutes=self.service.time)
        super().save(*args, **kwargs)

    def clean(self):
        """Валидация: время не может быть в прошлом при создании"""
        if self.date_start and self.date_start < timezone.now():
            raise ValidationError("Нельзя записаться на прошедшее время")

    class Meta:
        verbose_name = "Бронирование тренировки"
        verbose_name_plural = "Бронирования тренировок"
        ordering = ["-date_start"]
        indexes = [
            models.Index(fields=["user", "status"]),
            models.Index(fields=["coach", "date_start"]),
        ]

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
    is_verified = models.BooleanField("Проверен", default=False)

    class Meta:
        verbose_name = "Отзыв о тренере"
        verbose_name_plural = "Отзывы о тренерах"

    def __str__(self):
        return f"Отзыв о тренере {self.coach.first_name} {self.coach.last_name} / Рейтинг: {self.rating}"


class Workout(BaseDate, TimeAgoModelMixin, BaseDateRange):
    """
    Факт проведённой тренировки (история)
    """

    type = models.CharField(
        max_length=20,
        choices=WorkoutType.choices,
        default=WorkoutType.PERSONAL,
        verbose_name="Тип",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Клиент",
        related_name="workouts",
    )
    coach = models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Тренер",
        related_name="workouts",
    )
    service = models.ForeignKey(
        CoachService,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Услуга",
        related_name="workouts",
    )

    # Статус
    status = models.CharField(
        max_length=20,
        choices=WorkoutStatus.choices,
        default=WorkoutStatus.SCHEDULED,
        verbose_name="Статус",
    )

    class Meta:
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"
        ordering = ["-date_start"]
        indexes = [
            models.Index(fields=["user", "date_start"]),
            models.Index(fields=["coach", "date_start"]),
            models.Index(fields=["status", "date_start"]),
        ]

    def __str__(self):
        return f"{self.user.get_full_name()} — {self.coach} ({self.date_start.date()})"

    # def duration_minutes(self):
    #     """Длительность в минутах"""
    #     if self.date_start and self.date_end:
    #         return int((self.date_end - self.date_start).total_seconds() / 60)
    #     return self.service.time if self.service else 60
