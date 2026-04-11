import logging

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)

SITE_NAME = "STORIES"
ADMIN_EMAIL = getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@stories-salon.ru")
NOTIFY_EMAILS = getattr(settings, "FEEDBACK_NOTIFY_EMAILS", ["serj2656@yandex.ru"])


def send_html_email(
    subject: str,
    template: str,
    context: dict,
    to: list[str] | None = None,
):
    """
    Универсальная функция отправки HTML-писем.

    В dev-режиме (EMAIL_BACKEND = console) письмо выводится в терминал.
    В production — отправляется через SMTP.
    """
    html_content = render_to_string(template, {**context, "domain": SITE_NAME})

    email_msg = EmailMessage(
        subject=subject,
        body=html_content,
        from_email=ADMIN_EMAIL,
        to=to or NOTIFY_EMAILS,
    )
    email_msg.content_subtype = "html"

    try:
        email_msg.send()
        logger.info(f"Email отправлен: {subject} → {to or NOTIFY_EMAILS}")
    except Exception as e:
        logger.error(f"Ошибка отправки email '{subject}': {e}")
        raise


def send_feedback_email(name: str, phone: str, message: str = ""):
    """Уведомление админа о новой заявке с формы обратной связи."""
    send_html_email(
        subject=f"Новая заявка с сайта {SITE_NAME} от {name}",
        template="email/feedback_notification.html",
        context={
            "name": name,
            "phone": phone,
            "message": message,
        },
    )


def send_welcome_email(name: str, email: str, code: str = ""):
    """Приветственное письмо / код подтверждения."""
    send_html_email(
        subject=f"Добро пожаловать в {SITE_NAME}!",
        template="email/welcome_email_code.html",
        context={
            "name": name,
            "email": email,
            "code": code,
        },
        to=[email],
    )
