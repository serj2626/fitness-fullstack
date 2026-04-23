from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from common.models import BaseDate


class NotificationType(models.TextChoices):
    BOOKED_TRAINING = "booked_training", "Вы забронировали тренировку"
    PAID_TRAINING = "paid_training", "Оплатили тренировку"
    BOOKED_SUBSCRIPTION = "booked_subscription", "Забронировали абонемент"
    PAID_SUBSCRIPTION = "paid_subscription", "Оплатили абонемент"
    TRAINING_CANCELED = "training_canceled", "Тренировка отменена"
    COMMENT_PUBLISHED = "comment_published", "Ваш комментарий опубликован"
    COMMENT_MODERATION = "comment_moderation", "Ваш комментарий должен пройти модерацию"
    COMMENT_REJECTED = "comment_rejected", "Ваш комментарий не был опубликован"
    SUBSCRIPTION_EXPIRING = (
        "subscription_expiring",
        "Ваш абонемент приближается к концу",
    )
    TRAINING_REMINDER = "training_reminder", "Приближается дата вашей тренировки"
    FEEDBACK_RECEIVED = "feedback_received", "Мы получили ваше обращение"


class Notification(BaseDate):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
        verbose_name="Пользователь",
    )
    type = models.CharField(
        max_length=50, choices=NotificationType.choices, verbose_name="Тип уведомления"
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Тип связанного объекта",
    )
    object_id = models.UUIDField(
        null=True, blank=True, verbose_name="ID связанного объекта"
    )
    content_object = GenericForeignKey("content_type", "object_id")

    message = models.TextField(
        blank=True, verbose_name="Дополнительный текст (если нужен)"
    )
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self):
        return f"{self.user} — {self.get_type_display()}"


# training = Training.objects.get(id=1)
# Notification.objects.create(
#     user=training.client,
#     type=NotificationType.BOOKED_TRAINING,
#     content_object=training,
#     # message необязательно
# )
