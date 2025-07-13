import os
from datetime import datetime
from uuid import uuid4


def dynamic_upload_to(instance, filename):
    """
    Возвращает путь к загруженному файлу.
    """

    folder = instance.__class__.__name__.lower()
    ext = filename.split(".")[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join("uploads", folder, datetime.now().strftime("%Y/%m"), filename)


def dynamic_path_by_img_with_date(path: str) -> str:
    """
    Возвращает путь к загруженному файлу с учетом даты
    """

    def wrapper(instance, filename):
        folder = path.lower()
        ext = filename.split(".")[-1]
        filename = f"{uuid4().hex}.{ext}"
        name_class = instance.__class__.__name__.lower()
        return os.path.join(
            folder, name_class, datetime.now().strftime("%Y/%m"), filename
        )

    return wrapper


def dynamic_path_by_img(path: str | None = None) -> callable:
    """
    Возвращает путь к загруженному файлу
    """

    def wrapper(instance, filename):
        folder = path.lower() if path else "uploads"
        ext = filename.split(".")[-1]
        filename = f"{instance.pk}.{ext.lower()}"
        return f"{folder}/{instance.__class__.__name__.lower()}/{filename}"

    return wrapper
