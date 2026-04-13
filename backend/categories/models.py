from django.db import models

from common.mixins import AutoSlugMixin, NameMixin
from common.models import BaseOrder
from common.upload import compress_image


class Category(NameMixin, BaseOrder, AutoSlugMixin):
    description = models.TextField("Описание", max_length=5000, blank=True, null=True)
    image = models.ImageField(
        "Изображение", upload_to="categories/", blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"Категория {self.name}"
