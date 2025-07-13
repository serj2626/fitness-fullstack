import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timesince import timesince
from django_ckeditor_5.fields import CKEditor5Field


class BaseID(models.Model):
    """
    Базовая модель для всех моделей с идентификатором
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class BaseContent(models.Model):
    """
    Базовая модель для всех моделей с контентом
    """

    content = CKEditor5Field(blank=True, verbose_name="Описание", config_name="extends")

    class Meta:
        abstract = True


class BaseTitle(models.Model):
    """
    Базовая модель для всех моделей с заголовком
    """

    title = models.CharField(max_length=255, verbose_name="Заголовок")

    class Meta:
        abstract = True


class BaseDate(models.Model):
    """
    Базовая модель для всех моделей с датой
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True


class BaseReview(BaseID, BaseDate):
    """
    Базовая модель для всех моделей с отзывами
    """

    first_name = models.CharField("Имя", max_length=100, null=True, blank=True)
    last_name = models.CharField("Фамилия", max_length=100, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    rating = models.SmallIntegerField(
        "Рейтинг", default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField("Текст отзыва", max_length=5000, null=True, blank=True)
    verified = models.BooleanField("Проверен", default=False)

    @property
    def time_age(self):
        return timesince(self.created_at) + " назад"

    class Meta:
        abstract = True
