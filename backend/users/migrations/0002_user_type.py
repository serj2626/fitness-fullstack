# Generated by Django 5.1 on 2025-06-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="type",
            field=models.CharField(
                choices=[("client", "Клиент"), ("trainer", "Тренер")],
                default="client",
                max_length=20,
            ),
        ),
    ]
