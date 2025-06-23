from django.db import models
from django.contrib.auth import get_user_model
from common.models import BaseContent, BaseID, BaseDate, BaseReview
from common.types import (
    POSITIONS_TYPE,
    SESSION_DURATION_CHOICES,
    TRAINERS_RATES_TYPE,
    SOCIAL_NETWORKS_TYPE,
    SERVICES_TYPE,
)
from datetime import timedelta
from django.utils.timesince import timesince
from common.upload import compress_image
from common.upload_to import dynamic_upload_to
from common.validators import (
    validate_image_extension_and_format,
    validate_russian_phone,
)

User = get_user_model()


class Trainer(BaseID, BaseContent):
    """
    Тренер
    """

    position = models.CharField("Должность", max_length=100, choices=POSITIONS_TYPE)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    email = models.EmailField("Email", unique=True)
    phone = models.CharField(
        "Телефон", max_length=15, unique=True, validators=[validate_russian_phone]
    )
    keywords = models.TextField(
        "Ключевые слова",
        max_length=255,
        null=True,
        blank=True,
        help_text="Через запятую",
    )
    experience = models.PositiveSmallIntegerField(
        "Опыт работы", null=True, blank=True, default=0
    )
    avatar = models.ImageField(
        "Аватар",
        upload_to=dynamic_upload_to,
        blank=True,
        null=True,
        validators=[validate_image_extension_and_format],
    )

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_position_display()}"

    def save(self, *args, **kwargs):
        if self.avatar:
            self.avatar = compress_image(self.avatar)
        super().save(*args, **kwargs)


class TrainerImage(BaseID, BaseDate):
    """
    Фото тренера
    """

    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, verbose_name="тренер", related_name="images"
    )
    image = models.ImageField(
        "Фото",
        upload_to=dynamic_upload_to,
        null=True,
        blank=True,
        validators=[validate_image_extension_and_format],
    )
    alt = models.CharField(
        "Описание", max_length=255, blank=True, null=True, default="Описание"
    )

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Фото {self.trainer}"

    class Meta:
        verbose_name = "Фото тренера"
        verbose_name_plural = "Фото тренеров"


class TrainerRate(models.Model):
    """
    Цены индивидульных тренировок
    """

    title = models.CharField(
        "Название тарифа", max_length=100, choices=TRAINERS_RATES_TYPE, default="basic"
    )

    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name="rates", verbose_name="тренер"
    )
    count_minutes = models.SmallIntegerField(
        "Количество минут",
        choices=SESSION_DURATION_CHOICES,
        default=60,  # по умолчанию 60 минут
    )
    price = models.SmallIntegerField("Цена", default=1000)
    description = models.TextField("Описание тарифа", blank=True)

    class Meta:
        verbose_name = "Тариф тренера"
        verbose_name_plural = "Тарифы тренеров"
        ordering = ["-price"]

    def __str__(self):
        return (
            f"Индивидуальное занятие на {self.count_minutes} минут - тариф {self.title}"
        )


class TrainerSocialNetwork(models.Model):
    """
    Социальные сети тренера
    """

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name="social_networks",
        verbose_name="тренер",
    )
    social_network = models.CharField(
        "Социальная сеть", max_length=100, choices=SOCIAL_NETWORKS_TYPE
    )
    link = models.URLField("Ссылка")

    class Meta:
        verbose_name = "Социальная сеть тренера"
        verbose_name_plural = "Социальные сети тренеров"
        unique_together = ("trainer", "social_network")

    def __str__(self):
        return f"{self.trainer} - {self.social_network}"


# class TrainerService(models.Model):
#     """
#     Услуги тренера
#     """

#     trainer = models.ForeignKey(
#         Trainer,
#         on_delete=models.CASCADE,
#         related_name="services",
#         verbose_name="тренер",
#     )
#     service = models.CharField("Услуга", max_length=100, choices=SERVICES_TYPE)

#     class Meta:
#         verbose_name = "Услуга тренера"
#         verbose_name_plural = "Услуги тренеров"
#         unique_together = ("trainer", "service")

#     def __str__(self):
#         return f"{self.trainer} - {self.service}"

# class TrainerService(models.Model):
#     """
#     Услуги тренера
#     """

#     trainer = models.ForeignKey(
#         Trainer,
#         on_delete=models.CASCADE,
#         related_name="services",
#         verbose_name="тренер",
#     )
#     service = models.ForeignKey(
#         Service,
#         on_delete=models.CASCADE,
#         related_name="trainers",
#         verbose_name="услуга",
#     )

#     class Meta:
#         verbose_name = "Услуга тренера"
#         verbose_name_plural = "Услуги тренеров"

#     def __str__(self):
#         return f"{self.trainer} - {self.service}"


class TrainingSession(BaseID, BaseDate):
    """
    Забронировать занятие
    """

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="trainings",
        verbose_name="Тренер",
    )
    client = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="trainings"
    )
    rate = models.ForeignKey(
        TrainerRate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="trainings",
        verbose_name="Тариф",
    )
    start = models.DateTimeField("Дата начала")
    end = models.DateTimeField("Конец", blank=True, null=True)
    is_booked = models.BooleanField(default=False, verbose_name="Занято")

    def save(self, *args, **kwargs):
        if not self.end:
            self.end = self.start + timedelta(self.rate.count_minutes)
        super().save(*args, **kwargs)

    @property
    def time_age(self):
        return timesince(self.created_at)

    class Meta:
        unique_together = (
            "trainer",
            "start",
            "end",
        )  # чтобы один тренер не был дважды на одно время
        verbose_name = "Забронированное занятие"
        verbose_name_plural = "Забронированные занятия"

    def __str__(self):
        return f"{self.trainer} — {self.start} - {self.end} ({'Занято' if self.is_booked else 'Свободно'})"


class TrainerReviews(BaseReview):
    """
    Отзывы о тренерах
    """

    trainer = models.ForeignKey(
        Trainer,
        verbose_name="тренер",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    class Meta:
        verbose_name = "Отзыв о тренерах"
        verbose_name_plural = "Отзывы о тренерах"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Отзыв от {self.name}"

    # @property
    # def time_age(self):
    #     return timesince(self.created_at)
