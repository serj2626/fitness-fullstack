# Generated by Django 5.1 on 2025-06-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainers", "0002_trainersocialnetwork"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainerimage",
            name="alt",
            field=models.CharField(
                blank=True,
                default="Описание",
                max_length=255,
                null=True,
                verbose_name="Описание",
            ),
        ),
    ]
