# from celery import shared_task
# from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model

# User = get_user_model()

# from .models import Schedule


# @shared_task(bind=True)
# def book_class_task(self, schedule_id, user_id):
#     try:
#         schedule = Schedule.objects.get(pk=schedule_id)
#         user = User.objects.get(pk=user_id)
#         schedule.add_participant()

#         # Логика отправки подтверждения
#         send_confirmation_email(user, schedule)

#         return {
#             "status": "success",
#             "available_slots": schedule.available_slots,
#         }
#     except Exception as e:
#         raise self.retry(exc=e, countdown=60)
