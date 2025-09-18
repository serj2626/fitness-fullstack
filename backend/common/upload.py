from io import BytesIO
import uuid
from django.core.files.base import ContentFile
from PIL import Image
import logging

logger = logging.getLogger(__name__)


def compress_image(image_field):
    """
    Компрессия изображения
    """

    image = Image.open(image_field)
    buffer = BytesIO()
    image.save(buffer, format="webp", quality=90)
    image_field.save("image.webp", ContentFile(buffer.getvalue()), save=False)
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
        image_field.save(
            filename, ContentFile(output_buffer.getvalue()), save=False
        )

        return image_field

    except Exception as e:
        logger.error(f"Error compressing image: {e}")
        return image_field
