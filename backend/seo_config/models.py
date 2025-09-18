import os
from io import BytesIO

from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]
    if ext not in valid_extensions:
        raise ValidationError(
            f"Недопустимое расширение '{ext}'. Разрешены: jpg, jpeg, png, webp."
        )


class SEO(models.Model):
    """
    SEO модель
    """

    class ChangeFrequency(models.TextChoices):
        """
        Перечисление частоты обновления сайта
        """

        ALWAYS = "always", "Всегда"
        HOURLY = "hourly", "Каждый час"
        DAILY = "daily", "Ежедневно"
        WEEKLY = "weekly", "Еженедельно"
        MONTHLY = "monthly", "Ежемесячно"
        YEARLY = "yearly", "Ежегодно"
        NEVER = "never", "Никогда"

    slug = models.SlugField(
        "URL путь",
        max_length=255,
        unique=True,
        help_text="URL путь, например: about/ (без начального и конечного слэша)",
    )
    title = models.CharField(
        "Заголовок (title)",
        max_length=255,
        blank=True,
        help_text="Макс. 60 символов",
    )
    description = models.TextField(
        "Описание (meta description)",
        blank=True,
        help_text="Макс. 160 символов",
    )
    keywords = models.TextField(
        "Ключевые слова (meta keywords)",
        blank=True,
        null=True,
        help_text="Через запятую",
    )

    canonical_url = models.URLField(
        "Canonical URL",
        blank=True,
        null=True,
        help_text="Полный URL для canonical ссылки",
    )
    noindex = models.BooleanField(
        "Noindex", default=False, help_text="Запретить индексацию страницы"
    )
    nofollow = models.BooleanField(
        "Nofollow",
        default=False,
        help_text="Запретить переход по ссылкам на странице",
    )

    og_title = models.CharField("OG Заголовок", max_length=255, blank=True)
    og_description = models.TextField("OG Описание", blank=True)
    og_image = models.ImageField(
        "OG Изображение",
        upload_to="seo/",
        blank=True,
        null=True,
        validators=[validate_image_extension],
    )

    # Для sitemap
    priority = models.DecimalField(
        "Приоритет в sitemap",
        max_digits=2,
        decimal_places=1,
        default=0.5,
        help_text="От 0.1 до 1.0",
    )
    changefreq = models.CharField(
        "Частота изменений",
        max_length=10,
        choices=ChangeFrequency.choices,
        default=ChangeFrequency.WEEKLY,
    )
    lastmod = models.DateTimeField("Дата последнего изменения", auto_now=True)

    def save(self, *args, **kwargs):
        # Сжимаем og_image, если оно есть и изменено
        if self.og_image and hasattr(self.og_image, "file"):
            img = Image.open(self.og_image)
            img = img.convert("RGB")  # для webp/png совместимости
            output = BytesIO()
            img.save(output, format="JPEG", quality=75, optimize=True)
            output.seek(0)
            self.og_image = ContentFile(output.read(), self.og_image.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SEO: {self.slug}"

    class Meta:
        verbose_name = "SEO"
        verbose_name_plural = "SEO"
        ordering = ["slug"]


class RobotsTXT(models.Model):
    """
    Управление текстом robots.txt через админку.
    """

    text = models.TextField(
        verbose_name="Текст файла robots.txt",
        default=""" User-agent: *
                    Disallow: /admin/
                    Disallow: /api/
                    Sitemap: https://yourdomain.com/sitemap.xml
                    """,
        help_text="Текст файла robots.txt, который будет отдавать сервер.",
    )

    class Meta:
        verbose_name = "robots.txt"
        verbose_name_plural = "robots.txt"

    def __str__(self):
        return "robots.txt"
