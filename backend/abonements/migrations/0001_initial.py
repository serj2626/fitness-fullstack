# Generated by Django 5.1 on 2025-06-20 12:30

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Abonement",
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
                    "title",
                    models.CharField(
                        choices=[
                            ("basic", "Базовый"),
                            ("vip", "VIP"),
                            ("premium", "Премиум"),
                        ],
                        default="basic",
                        max_length=100,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "price",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="Цена"
                    ),
                ),
                (
                    "number_of_months",
                    models.SmallIntegerField(verbose_name="Количество месяцев"),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Абонемент",
                "verbose_name_plural": "Абонементы",
                "ordering": ["price"],
            },
        ),
        migrations.CreateModel(
            name="AbonementService",
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
                    "title",
                    models.CharField(
                        choices=[
                            ("gym", "Тренажерный зал"),
                            ("pool", "Бассейн"),
                            ("yoga", "Йога"),
                            ("spa", "SPA"),
                            ("cosmetology", "Косметология"),
                            ("cycle", "Велотренажер"),
                            ("water aerobics", "Водное аэробик"),
                            ("dancing", "Танцы"),
                        ],
                        max_length=100,
                        verbose_name="Название",
                    ),
                ),
                (
                    "abonement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to="abonements.abonement",
                        verbose_name="Абонемент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Услуга абонемента",
                "verbose_name_plural": "Услуги абонементов",
            },
        ),
        migrations.CreateModel(
            name="OrderAbonement",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                ("start", models.DateField(verbose_name="Начало абонемента")),
                (
                    "end",
                    models.DateField(
                        blank=True, null=True, verbose_name="Конец абонемента"
                    ),
                ),
                ("status", models.BooleanField(default=False, verbose_name="Оплачен")),
                ("active", models.BooleanField(default=False, verbose_name="Активен")),
                (
                    "abonement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="abonements.abonement",
                        verbose_name="Абонемент",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="abonements",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Клиент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Забронированный абонемент",
                "verbose_name_plural": "Забронированные абонементы",
            },
        ),
        migrations.CreateModel(
            name="GymVisit",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "visit_start",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время начала визита"
                    ),
                ),
                (
                    "visit_end",
                    models.DateTimeField(
                        auto_now=True,
                        null=True,
                        verbose_name="Дата и время окончания визита",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gym_visits",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "order_abonement",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="visits",
                        to="abonements.orderabonement",
                        verbose_name="Абонемент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Визит в фитнес-клуб",
                "verbose_name_plural": "Визиты в фитнес-клуб",
                "ordering": ["-visit_start"],
            },
        ),
    ]
