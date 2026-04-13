from django.db import models

from common.mixins import AutoSlugMixin
from common.models import BaseContent, BaseDate
from common.upload import compress_image


class Post(BaseContent, BaseDate, AutoSlugMixin):

    PostType = [
        ("news", "Новость"),
        ("article", "Статья"),
    ]
    title = models.TextField("Заголовок", max_length=500, unique=True)
    type = models.CharField("Тип", max_length=255, choices=PostType, default="article")

    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"Пост {self.title}"

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/posts/{self.slug}/"
