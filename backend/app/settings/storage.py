import os
from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage

class CKEditor5Storage(FileSystemStorage):
    """
    Кастомное хранилище для файлов django-ckeditor-5.
    Все файлы будут сохраняться в MEDIA_ROOT/editor/
    и будут доступны по URL /media/editor/...
    """
    def __init__(self, *args, **kwargs):
        # Указываем папку для хранения файлов редактора
        self.location = os.path.join(settings.MEDIA_ROOT, "editor")
        self.base_url = urljoin(settings.MEDIA_URL, "editor/")
        super().__init__(*args, **kwargs)

