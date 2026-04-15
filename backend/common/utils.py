import re
from io import BytesIO

from django.core.files.base import ContentFile
from django.utils.text import slugify
from PIL import Image
from rest_framework import serializers
from transliterate import translit


def ru_slugify(value: str) -> str:
    translit = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "sch",
        "ь": "",
        "ы": "y",
        "ъ": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }
    value = "".join(translit.get(c, c) for c in value.lower())
    return slugify(re.sub(r"[^a-z0-9\s-]", "", value))


def make_slug(*args):
    """
    Создаёт slug из одного или нескольких полей.
    Аргументы могут быть строками или числами.
    """

    # Объединяем все аргументы в одну строку через пробел
    combined = " ".join(str(arg) for arg in args if arg is not None)

    # Транслитерируем кириллицу в латиницу (переводим русский текст)
    transliterated = translit(combined, "ru", reversed=True)

    # Переводим в нижний регистр
    lowered = transliterated.lower()

    # Заменяем все небуквенно-цифровые символы на дефисы
    replaced = re.sub(r"[^a-z0-9]+", "-", lowered)

    # Убираем начальные и конечные дефисы
    cleaned = replaced.strip("-")

    # Убираем повторяющиеся дефисы
    slug = re.sub(r"-{2,}", "-", cleaned)

    return slug


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


class RelativeOnlyImageField(serializers.ImageField):
    """
    Поле для изображений, которое сохраняет только имя файла
    """

    def to_representation(self, value):
        if not value:
            return None
        return value.name


def get_cache_ttl(minutes: int = 5):
    return minutes * 60


class RelativeOnlyFileField(serializers.FileField):
    """
    Поле для файлов, которое возвращает относительный путь (value.name),
    без абсолютного URL
    """

    def to_representation(self, value):
        if not value:
            return None
        return value.name


def get_review_text(value: str | None = None) -> str:
    """
    Генерирует текст отзывв/обратной связи  в админке Django.

    :param value: Текст отзыва
    :return: текст
    """
    if not value:
        return "Текст отсутствует"
    return value if len(value) < 26 else str(value)[:26] + "..."
