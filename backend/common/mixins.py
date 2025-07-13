import io

from django.core.exceptions import MultipleObjectsReturned
from django.utils.html import format_html
from PIL import Image
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView


class WebpImageMixin:
    """
    Миксин для сжатия изображений
    """

    def save(self, *args, **kwargs):
        if hasattr(self, "image") and self.image:
            img = Image.open(self.image)
            buffer = io.BytesIO()
            img.save(buffer, format="webp", quality=90)
            self.image.save("image.webp", buffer, save=False)
        super().save(*args, **kwargs)


class SingletonAdminInfoMixin:
    """
    Миксин для отображения дополнительной информации в админке
    """

    singleton_info_text = "Можно создать только один экземпляр"
    singleton_info_color = "red"
    singleton_limit = 1

    def get_desc(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            self.singleton_info_color,
            self.singleton_info_text,
        )

    get_desc.short_description = "Доп Инфа"

    def has_add_permission(self, request):
        return self.model.objects.count() < self.singleton_limit


class BaseSectionViewMixin(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        try:
            instance = self.model.objects.get()
        except self.model.DoesNotExist:
            raise NotFound(detail=f"{self.model.__name__} not found.")
        except MultipleObjectsReturned:
            raise NotFound(
                detail=f"Multiple {self.model.__name__} objects found. Only one expected."
            )

        serializer = self.serializer_class(instance)
        return Response(serializer.data)
