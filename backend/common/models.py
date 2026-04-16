import uuid

from django.db import models
from django.utils.timesince import timesince
from django_ckeditor_5.fields import CKEditor5Field


class BaseOrder(models.Model):
    """
    Базовая модель для всех моделей с порядковым номером
    """

    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Порядковый номер",
        help_text="Полезно для сортировки | чем больше число, тем дальше на странице",
    )

    class Meta:
        abstract = True


class BaseID(models.Model):
    """
    Базовая модель для всех моделей с идентификатором
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class BaseContent(models.Model):
    """
    Базовая модель для всех моделей с контентом
    """

    content = CKEditor5Field(blank=True, verbose_name="Контент", config_name="extends")

    class Meta:
        abstract = True


class BaseTitle(models.Model):
    """
    Базовая модель для всех моделей с заголовком
    """

    title = models.CharField(max_length=255, verbose_name="Заголовок")

    class Meta:
        abstract = True


class BaseDescription(models.Model):
    """
    Базовая модель для всех моделей с описанием
    """

    description = models.TextField(
        max_length=2500, verbose_name="Описание", blank=True, null=True
    )

    class Meta:
        abstract = True


class BaseEmail(models.Model):
    """
    Базовая модель для всех моделей с описанием
    """

    email = models.EmailField(max_length=255, verbose_name="Почта")

    class Meta:
        abstract = True


class BaseDate(models.Model):
    """
    Базовая модель для всех моделей с датой
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True


class BaseDateRange(models.Model):
    """
    Базовая модель диапазона дат
    """

    date_start = models.DateField("Дата начала", blank=True, null=True)
    date_end = models.DateField("Дата окончания", blank=True, null=True)

    class Meta:
        abstract = True


class BaseReview(BaseID, BaseDate):
    """
    Базовая модель для всех моделей с отзывами
    """

    first_name = models.CharField("Имя", max_length=100, null=True, blank=True)
    last_name = models.CharField("Фамилия", max_length=100, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    position = models.CharField("Должность", max_length=100, null=True, blank=True)
    text = models.TextField("Текст отзыва", max_length=5000, null=True, blank=True)
    verified = models.BooleanField("Проверен", default=False)

    @property
    def time_age(self):
        return timesince(self.created_at) + " назад"

    class Meta:
        abstract = True


# class BaseFeedBack(BaseDate):
#     """
#     Базовая модель для всех моделей с обратной связью
#     """

#     theme = models.CharField("Тема", max_length=255)
#     name = models.CharField("Имя", max_length=255)
#     phone = models.CharField("Телефон", max_length=255)
#     email = models.EmailField("Email")
#     message = models.TextField("Сообщение", max_length=5000)
#     verified = models.BooleanField("Проверен", default=False)

#     class Meta:
#         abstract = True


# import os

# from django.db import models
# from django.db.models.signals import post_delete, pre_save
# from django.dispatch import receiver


# class AutoDeleteFileMixin(models.Model):
#     """
#     Миксин для автоматического удаления файлов (ImageField / FileField)
#     при удалении модели или замене файла.
#     """

#     class Meta:
#         abstract = True

#     @classmethod
#     def _get_file_fields(cls):
#         """Возвращает список всех FileField / ImageField в модели"""
#         return [
#             field
#             for field in cls._meta.fields
#             if isinstance(field, (models.FileField, models.ImageField))
#         ]


# # 🗑 Удаление файла при удалении модели
# @receiver(post_delete)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     if not issubclass(sender, AutoDeleteFileMixin):
#         return

#     for field in sender._get_file_fields():
#         file = getattr(instance, field.name)
#         if file and os.path.isfile(file.path):
#             os.remove(file.path)


# # 🔄 Удаление старого файла при обновлении
# @receiver(pre_save)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     if not issubclass(sender, AutoDeleteFileMixin) or not instance.pk:
#         return

#     try:
#         old_instance = sender.objects.get(pk=instance.pk)
#     except sender.DoesNotExist:
#         return

#     for field in sender._get_file_fields():
#         old_file = getattr(old_instance, field.name)
#         new_file = getattr(instance, field.name)

#         if old_file and old_file != new_file and os.path.isfile(old_file.path):
#             os.remove(old_file.path)
