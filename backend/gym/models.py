from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from common.models import BaseContent, BaseDate, BaseID, BaseReview, BaseTitle
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
