from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from common.mixins import WebpImageMixin
from common.models import (
    BaseContent,
    BaseDate,
    BaseDescription,
    BaseID,
    BaseReview,
    BaseTitle,
)
from django.core.validators import MinValueValidator, MaxValueValidator

from common.types import SERVICES_TYPE
from common.upload import compress_image
from common.upload_to import dynamic_upload_to
from common.validators import validate_image_extension_and_format, validate_svg


User = get_user_model()


class Post(BaseTitle, BaseDate, BaseContent):
    """
    Пост
    """

    POST_CATEGORIES = [
        ("workout", "Тренировки"),
        ("nutrition", "Питание"),
        ("news", "Новости клуба"),
        ("promo", "Акции"),
    ]
    slug = models.SlugField(
        "URL", max_length=200, unique=True, blank=True, null=True
    )
    category = models.CharField(
        "Категория", max_length=20, choices=POST_CATEGORIES
    )
    image = models.ImageField(
        "Изображение", upload_to="posts/previews/", blank=True, null=True
    )
    is_published = models.BooleanField("Опубликовано", default=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Service(BaseID):
    """
    Услуга
    """

    type = models.CharField(
        "Тип", max_length=100, choices=SERVICES_TYPE, default="gym"
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    avatar = models.ImageField(
        "Фото",
        upload_to=dynamic_upload_to,
        blank=True,
        null=True,
        validators=[validate_image_extension_and_format],
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.type)
        if self.avatar:
            self.avatar = compress_image(self.avatar)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Услуга {self.get_type_display()}"


class GymReviews(BaseReview):
    """
    Отзывы о тренажерном зале
    """

    class Meta:
        verbose_name = "Отзыв о тренажерном зале"
        verbose_name_plural = "Отзывы о тренажерном зале"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Отзыв"


class FAQ(models.Model):
    """
    Модель вопросов и ответов
    """

    question = models.TextField("Вопрос")
    answer = models.TextField(
        "Ответ",
        default="Здравствуйте",
        help_text="Максимум 1000 символов",
    )

    class Meta:
        verbose_name = "Вопрос и ответ"
        verbose_name_plural = "Вопросы и ответы"

    def __str__(self):
        return f"Вопрос {self.question}"


class Advantage(BaseTitle, BaseDate):
    """
    Преимущество
    """

    description = models.TextField("Описание")
    icon = models.FileField(
        "Иконка",
        upload_to="advantages/icons/",
        validators=[validate_svg],
    )
    alt = models.CharField("Описание к иконке", max_length=255)

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    def __str__(self):
        return f'Преимущество "{self.title}"'


class Equipment(WebpImageMixin, BaseTitle, BaseDescription):
    """
    Оборудование
    """

    image = models.ImageField(
        "Изображение", blank=True, null=True, upload_to="equipment/"
    )
    services = models.TextField(
        "услуги",
        max_length=255,
        null=True,
        blank=True,
        help_text="Через запятую",
    )

    class Meta:
        verbose_name = "Наши залы и оборудование"
        verbose_name_plural = "Наши залы и оборудование"

    def save(self, *args, **kwargs):
        WebpImageMixin.save(self, *args, **kwargs)
        if self.services:
            self.services = (
                str(self.services)
                .replace(",   ", ",")
                .replace(",  ", ",")
                .replace(", ", ",")
            )
        super(Equipment, self).save(*args, **kwargs)

    def __str__(self):
        return f"Оборудование {self.title}"


class Schedule(BaseDate):
    """
    Расписание
    """

    trainer = models.ForeignKey(
        "trainers.Trainer",
        verbose_name="Тренер",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="schedules",
    )
    service = models.ForeignKey(
        Service,
        verbose_name="Услуга",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date = models.DateField("Дата")
    start = models.TimeField("Время начала")
    end = models.TimeField("Время окончания")
    max_participants = models.PositiveSmallIntegerField(
        "Максимальное количество участников",
        default=10,
        validators=[MinValueValidator(1), MaxValueValidator(20)],
    )
    current_participants = models.PositiveSmallIntegerField(
        "Текущее количество участников", default=0, editable=False
    )
    status = models.BooleanField("Активно", default=True)

    def add_participant(self):
        if self.current_participants >= self.max_participants:
            raise ValidationError("Нет свободных мест")
        self.current_participants += 1
        self.save()

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
        ordering = ['date', 'start']

    def clean(self):
        super().clean()

        # 1. Проверка даты (не сегодня и не в прошлом)
        if self.date <= timezone.now().date():
            raise ValidationError(
                {'date': 'Дата занятия должна быть в будущем'}
            )

        # 2. Проверка времени окончания > времени начала
        if self.end <= self.start:
            raise ValidationError(
                {'end': 'Время окончания должно быть позже времени начала'}
            )

        # 3. Проверка длительности занятия (45-75 минут)
        duration = timedelta(
            hours=self.end.hour - self.start.hour,
            minutes=self.end.minute - self.start.minute,
        )
        if not (timedelta(minutes=45) <= duration <= timedelta(minutes=75)):
            raise ValidationError(
                {'end': 'Длительность занятия должна быть от 45 до 75 минут'}
            )

        # 4. Проверка максимального количества участников (не более 20)
        if self.max_participants > 20:
            raise ValidationError(
                {'max_participants': 'Максимальное количество участников - 20'}
            )

        # 5. Проверка что текущих участников не больше максимального
        if self.current_participants > self.max_participants:
            raise ValidationError(
                {
                    'current_participants': 'Количество участников превышает максимальное'
                }
            )

        # 6. Проверка пересечений времени для тренера
        if self.trainer and self.date and self.start and self.end:
            overlapping = Schedule.objects.filter(
                trainer=self.trainer,
                date=self.date,
                start__lt=self.end,
                end__gt=self.start,
                status=True,
            ).exclude(pk=self.pk if self.pk else None)

            if overlapping.exists():
                raise ValidationError('Тренер уже занят в это время')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def available_slots(self) -> int:
        """Количество свободных мест"""
        return self.max_participants - self.current_participants

    def __str__(self):
        return f"{self.date} {self.start}-{self.end}: {self.trainer}"


class RecordOnSchedule(BaseDate):
    """
    Запись на групповое занятие
    """

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.schedule} - {self.user}"

    class Meta:
        verbose_name = "Запись на групповое занятие"
        verbose_name_plural = "Записи на групповое занятие"
        unique_together = ("schedule", "user")
