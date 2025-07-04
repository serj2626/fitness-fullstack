# Generated by Django 5.1 on 2025-06-20 12:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("abonements", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Сумма"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Ожидает оплаты"),
                            ("completed", "Оплачен"),
                            ("failed", "Ошибка оплаты"),
                            ("refunded", "Возврат"),
                        ],
                        default="pending",
                        max_length=20,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("card", "Карта"),
                            ("cash", "Наличные"),
                            ("transfer", "Перевод"),
                        ],
                        default="card",
                        max_length=20,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                (
                    "payment_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата оплаты"
                    ),
                ),
                (
                    "transaction_id",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="ID транзакции",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to="abonements.orderabonement",
                        verbose_name="Заказ",
                    ),
                ),
            ],
            options={
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
                "ordering": ["-created_at"],
            },
        ),
    ]
