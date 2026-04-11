# ─── Celery tasks для contacts ─────────────────────────────────────
# Раскомментировать когда Celery + Redis запущены.
#
# from celery import shared_task
# from common.mail import send_feedback_email, send_welcome_email
#
#
# @shared_task(bind=True, max_retries=3, default_retry_delay=60)
# def send_feedback_email_task(self, name: str, phone: str, message: str = ""):
#     """
#     Асинхронная отправка email-уведомления о новой заявке.
#     Retry до 3 раз с интервалом 60 сек при ошибке.
#     """
#     try:
#         send_feedback_email(name=name, phone=phone, message=message)
#     except Exception as exc:
#         self.retry(exc=exc)
#
#
# @shared_task(bind=True, max_retries=3, default_retry_delay=60)
# def send_welcome_email_task(self, name: str, email: str, code: str = ""):
#     """Асинхронная отправка приветственного письма."""
#     try:
#         send_welcome_email(name=name, email=email, code=code)
#     except Exception as exc:
#         self.retry(exc=exc)
#
#
# ─── Использование в views.py: ────────────────────────────────────
# Вместо прямого вызова:
#   send_feedback_email(name=..., phone=..., message=...)
# Использовать:
#   send_feedback_email_task.delay(name=..., phone=..., message=...)
#
# Это отправит задачу в Redis-очередь и Celery-worker выполнит её
# в фоне, не блокируя HTTP-ответ пользователю.
#
# ─── Запуск Celery worker (в отдельном терминале): ─────────────────
# celery -A app worker --loglevel=info
#
# ─── Запуск Celery beat (для периодических задач): ─────────────────
# celery -A app beat --loglevel=info
