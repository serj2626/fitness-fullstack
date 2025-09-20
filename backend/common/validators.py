import re
from django.template.defaultfilters import filesizeformat
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from PIL import Image

phone_regex = re.compile(r"^\+?7?\d{10}$")


phone_validator = RegexValidator(
    regex=phone_regex,
    message="Неправильный формат телефонного номера. Пример: +7 123 456 78 90 или 89123456789",
)


def validate_russian_phone(value):
    # Удаляем пробелы, дефисы, скобки
    cleaned = re.sub(r"[^\d+]", "", value)

    # Проверка на соответствие формату +7XXXXXXXXXX или 8XXXXXXXXXX
    if re.fullmatch(r"(\+7|8)\d{10}", cleaned) is None:
        raise ValidationError(
            _(
                "Введите корректный российский номер телефона в формате +7XXXXXXXXXX или 8XXXXXXXXXX"
            ),
            params={"value": value},
        )


def validate_image_extension_and_format(image):
    # 1. Проверка расширения (в нижнем регистре)
    valid_extensions = ["jpeg", "png", "jpg", "webp"]
    ext = image.name.split(".")[-1].lower()
    if ext not in valid_extensions:
        raise ValidationError(
            f"Недопустимое расширение файла: .{ext}. Разрешены: {', '.join(valid_extensions)}"
        )

    # 2. Проверка содержимого файла (формата изображения)
    try:
        img = Image.open(image)
        if (
            str(img.format).lower() not in valid_extensions
            and img.format not in valid_extensions
        ):
            raise ValidationError(
                f"Недопустимый формат изображения: {img.format}. Допустимы: JPEG, PNG."
            )
    except Exception:
        raise ValidationError(
            "Не удалось открыть изображение. Убедитесь, что файл — это допустимое изображение."
        )


def validate_svg(file):
    valid_extensions = ['.svg']
    name = file.name.lower()

    if not any(name.endswith(ext) for ext in valid_extensions):
        raise ValidationError("Файл должен быть в формате SVG.")

    # Проверим содержимое (начало файла)
    try:
        content = file.read().decode("utf-8")
        if '<svg' not in content:
            raise ValidationError("Файл не является допустимым SVG.")
    except Exception:
        raise ValidationError("Ошибка при чтении SVG файла.")

    # Важно: вернем указатель в начало
    file.seek(0)


def validate_image_size(value):
    """
    Проверка размера изображения
    """

    filesize = value.size
    max_size = 2 * 1024 * 1024  # 2MB
    if filesize > max_size:
        raise ValidationError(
            f'Максимальный размер файла {filesizeformat(max_size)}. '
            f'Ваш файл {filesizeformat(filesize)}'
        )
