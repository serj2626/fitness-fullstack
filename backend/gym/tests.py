from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Schedule


class ScheduleTestCase(TestCase):
    def setUp(self):
        self.schedule = Schedule.objects.create(
            date="2023-12-31", start="10:00", end="11:30", max_participants=2
        )

    def test_add_participant(self):
        # Первый участник
        self.schedule.add_participant()
        self.assertEqual(self.schedule.current_participants, 1)

        # Второй участник
        self.schedule.add_participant()
        self.assertEqual(self.schedule.current_participants, 2)

        # Попытка добавить третьего
        with self.assertRaises(ValidationError):
            self.schedule.add_participant()
