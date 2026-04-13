import logging
import uuid
from io import BytesIO
from uuid import uuid4

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from PIL import Image


class CustomStorage(FileSystemStorage):
    # Ваша кастомная логика storage
    pass


def compress_image(image_field, quality=90):
    image = Image.open(image_field)
    buffer = BytesIO()
    image.save(buffer, format="WEBP", quality=quality)

    # Генерируем новое имя
    original_name = os.path.basename(image_field.name)
    name_without_ext = os.path.splitext(original_name)[0]
    new_name = f"{name_without_ext}_{uuid4().hex}.webp"

    image_field.save(new_name, ContentFile(buffer.getvalue()), save=False)
    return image_field


def compress_img(image_field, quality=90, format="WEBP"):
    """
    Компрессия изображения с генерацией уникального имени файла через UUID

    :param image_field: Поле ImageField модели Django
    :param quality: Качество сжатия (1-100)
    :param format: Формат сохранения (WEBP, JPEG, etc)
    :return: Сжатое изображение (готово для сохранения в поле)
    """
    if not image_field:
        return None

    try:
        img = Image.open(image_field)

        # Конвертируем в RGB если это PNG с прозрачностью
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        output_buffer = BytesIO()
        img.save(output_buffer, format=format, quality=quality, optimize=True)

        # Генерируем уникальное имя файла с UUID
        ext = format.lower()
        filename = f"{uuid.uuid4()}.{ext}"

        # Сохраняем в поле
        image_field.save(filename, ContentFile(output_buffer.getvalue()), save=False)

        return image_field

    except Exception as e:
        logging.error(f"Error compressing image: {e}")
        return image_field


import os
from datetime import datetime

from django.conf import settings
from django.utils.deconstruct import deconstructible


@deconstructible
class CustomStorage(FileSystemStorage):
    """
    Кастомное хранилище для CKEditor5.
    Загруженные файлы будут сохраняться в /media/uploads/ckeditor/YYYY/MM/DD/
    и доступны по URL /media/uploads/ckeditor/...
    """

    def __init__(self, location=None, base_url=None):
        # Папка, куда сохраняются файлы
        location = location or os.path.join(settings.MEDIA_ROOT, "uploads/ckeditor")
        base_url = base_url or f"{settings.MEDIA_URL}uploads/ckeditor/"
        super().__init__(location, base_url)

    def get_available_name(self, name, max_length=None):
        """
        Если файл с таким именем уже есть — добавляем уникальный суффикс.
        """
        if self.exists(name):
            base, ext = os.path.splitext(name)
            name = f"{base}_{datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"
        return name

    def _save(self, name, content):
        """
        При сохранении создаем поддиректорию по дате: /YYYY/MM/DD/
        """
        date_path = datetime.now().strftime("%Y/%m/%d")
        name = os.path.join(date_path, name)
        return super()._save(name, content)
