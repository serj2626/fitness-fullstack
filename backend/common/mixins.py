from django.contrib import admin, messages
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.timesince import timesince
from rest_framework import serializers

from .utils import ru_slugify as slugify


class TimeAgoModelMixin:
    """
    Миксин для добавления свойства time к моделям,
    которое показывает время, прошедшее с создания объекта
    """

    @property
    def time(self):
        """Возвращает время, прошедшее с создания объекта"""
        if hasattr(self, "created_at") and self.created_at:
            full_time = timesince(self.created_at)
            short_time = full_time.split(",")[0]
            return f"{short_time} назад" if short_time[0] != "0" else "только что"
        return "только что"

    # @property
    # def time(self):
    #     """Возвращает время, прошедшее с создания объекта"""
    #     if hasattr(self, 'created_at') and self.created_at:
    #         return f"{timesince(self.created_at)} назад"
    #     return "время неизвестно"

    # @property
    # def time_short(self):
    #     """Короткая версия времени (только первая единица)"""
    #     if hasattr(self, 'created_at') and self.created_at:
    #         full_time = timesince(self.created_at)
    #         # Берем только первую часть (например, "2 дня" вместо "2 дня, 3 часа")
    #         short_time = full_time.split(',')[0]
    #         return f"{short_time} назад"
    #     return "только что"


class NameMixin(models.Model):
    name = models.CharField("Название", max_length=350, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.name:
            self.name = str(self.name).capitalize()
        super().save(*args, **kwargs)


class AutoSlugMixin(models.Model):
    slug = models.SlugField("Слаг", max_length=255, unique=True, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # 1. Определяем имя поля-источника
        source_field = "name" if hasattr(self, "name") else "title"
        new_value = getattr(self, source_field, None)

        if self.pk:
            # 2. Достаем старое значение ПРЯМО из базы (чистый SQL запрос)
            # Это исключает влияние данных, пришедших из формы админки
            print("asdsadasd", type(self))
            old_value = (
                type(self)
                .objects.filter(pk=self.pk)
                .values_list(source_field, flat=True)
                .first()
            )

            # 3. Если значение изменилось — принудительно пересоздаем слаг
            if new_value != old_value:
                self.slug = slugify(new_value)

        # 4. Если это создание нового объекта
        elif not self.slug and new_value:
            self.slug = slugify(new_value)

        super().save(*args, **kwargs)


class AdminImagePreviewMixin:
    """
    Миксин для отображения изображений в админке
    """

    image_field_name = "image"
    image_preview_width = 80
    image_preview_height = 80
    image_large_preview_width = 150
    image_large_preview_height = 150
    image_style = "border-radius: 50%;"

    def get_image(self, obj):
        image_field = getattr(obj, self.image_field_name, None)
        if image_field and hasattr(image_field, "url"):
            return mark_safe(
                f'<img src="{image_field.url}" '
                f'alt="Ваше фото отсутствует в  папке media" '
                f'style="{self.image_style}" '
                f'width="{self.image_preview_width}" height="{self.image_preview_height}">'
            )
        return "Нет изображения"

    def get_large_image(self, obj):
        image_field = getattr(obj, self.image_field_name, None)
        if image_field and hasattr(image_field, "url"):
            return mark_safe(
                f'<img src="{image_field.url}" '
                f'alt="Ваше фото отсутствует в  папке media" '
                f'style="{self.image_style}" '
                f'width="{self.image_large_preview_width}" height="{self.image_large_preview_height}">'
            )
        return "Нет изображения"

    get_image.short_description = "Фото"
    get_large_image.short_description = "Превью фото"


class ChildrenMixin(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        if obj.children.exists():
            # рекурсивный вызов: используем текущий сериализатор
            serializer = self.__class__(
                obj.children.all(), many=True, context=self.context
            )
            return serializer.data
        return []

    class Meta:
        abstract = True


class SingletonAdminInfoMixin:
    """
    Миксин для отображения дополнительной информации в админке
    """

    singleton_info_color = "red"
    singleton_limit = 1
    singleton_info_text = f"Ограничение: {singleton_limit}"

    def get_desc(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            self.singleton_info_color,
            self.singleton_info_text,
        )

    get_desc.short_description = "Доп Инфа"

    def has_add_permission(self, request):
        return self.model.objects.count() < self.singleton_limit


class MaxObjectsMixin:
    """
    Миксин для ограничения максимального количества объектов в модели.
    """

    max_objects = None  # Установите нужное значение в наследуемом классе
    error_message = f"Невозможно создать больше {max_objects} объектов."

    def has_add_permission(self, request):
        """
        Проверяет, можно ли добавить новый объект.
        """
        if self.max_objects is None:
            return super().has_add_permission(request)

        # Получаем количество существующих объектов
        current_count = self.model.objects.count()

        # Если достигнут лимит, запрещаем добавление
        if current_count >= self.max_objects:
            return False

        return super().has_add_permission(request)

    def save_model(self, request, obj, form, change):
        """
        Проверяем при сохранении (для случаев прямого доступа к URL).
        """
        if not change and self.max_objects is not None:  # Только для новых объектов
            current_count = self.model.objects.count()
            if current_count >= self.max_objects:
                messages.error(
                    request, self.error_message.format(max_objects=self.max_objects)
                )
                return  # Не сохраняем объект

        super().save_model(request, obj, form, change)


class Admin:
    description_title = ""
    returned_title = ""

    @admin.display(description="Заказ от")
    def order_by_time(self, obj):
        date = obj.created_at.strftime("%d.%m.%Y")
        return f"{self.returned_title} от {date}"
