from django.utils.safestring import mark_safe


class AdminImagePreviewMixin:
    """
    Миксин для отображения изображений в админке
    """

    image_field_name = "image"
    image_preview_width = 50
    image_preview_height = 50
    image_style = "border-radius: 50%;"

    def get_image(self, obj):
        image_field = getattr(obj, self.image_field_name, None)
        if image_field and hasattr(image_field, "url"):
            return mark_safe(
                f'<img src="{image_field.url}" '
                f'style="{self.image_style}" '
                f'width="{self.image_preview_width}" height="{self.image_preview_height}">'
            )
        return "Нет изображения"

    get_image.short_description = "Фото"


class AdminLimitMixin:
    """
    Миксин для ограничения количества экземпляров в админке
    """

    singleton_limit = 1

    def has_add_permission(self, request):
        return self.model.objects.count() < self.singleton_limit


class AdminShortDescriptionMixin:
    """
    Миксин для отображения короткого описания в админке
    """

    description_field_name = "description"
    description_length = 26

    def get_description(self, obj):
        value = getattr(obj, self.description_field_name, "")
        if not value:
            return "Нет описания"
        return f"{str(value)[:self.description_length]}..."

    get_description.short_description = "Описание"
