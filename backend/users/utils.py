from django.conf import settings
from django.core.mail import send_mail

from .models import CreateCodeSendEmail


def send_verification_email(email, code):
    """Отправляет письмо с кодом"""
    subject = "Код подтверждения регистрации"
    message = f"Ваш код подтверждения: {code}\nКод действителен 30 минут."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


def create_verification_code(user):
    """
    1. Удаляет старые коды пользователя
    2. Создаёт новый (модель сама сгенерирует код в save())
    3. Отправляет письмо
    """
    # Удаляем старые неиспользованные коды
    CreateCodeSendEmail.objects.filter(user=user, is_used=False).delete()

    # Создаём новый (код сгенерируется в модели)
    code_obj = CreateCodeSendEmail.objects.create(user=user)

    # Отправляем письмо
    send_verification_email(user.email, code_obj.code)

    return code_obj
