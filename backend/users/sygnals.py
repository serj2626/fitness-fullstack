from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfileQuestionnaire


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_questionnaire(sender, instance, created, **kwargs):
    if created:
        UserProfileQuestionnaire.objects.create(user=instance)
