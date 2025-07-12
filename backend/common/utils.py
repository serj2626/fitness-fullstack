from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


def compress_variants(image_field):
    """
    Возвращает три версии изображения:
    1. Оригинал
    2. Сжатое (качество 90)
    3. Сильно сжатое (качество 50)
    """

    original = image_field

    def compress(quality):
        image = Image.open(image_field)
        buffer = BytesIO()
        image.save(buffer, format="webp", quality=quality)
        return ContentFile(buffer.getvalue(), name=f"image_q{quality}.webp")

    compressed = compress(90)
    heavily_compressed = compress(50)

    return original, compressed, heavily_compressed


def resize_variants(image_field):
    """
    Возвращает изображения разных размеров (ширина):
    1. Маленькое (300px)
    2. Среднее (600px)
    3. Большое (1024px)
    """

    def resize(width):
        image = Image.open(image_field)
        image = image.convert("RGB")  # обязательно для webp
        aspect_ratio = image.height / image.width
        new_height = int(width * aspect_ratio)
        resized = image.resize((width, new_height), Image.LANCZOS)
        buffer = BytesIO()
        resized.save(buffer, format="webp", quality=85)
        return ContentFile(buffer.getvalue(), name=f"image_{width}.webp")

    small = resize(300)
    medium = resize(600)
    large = resize(1024)

    return small, medium, large
