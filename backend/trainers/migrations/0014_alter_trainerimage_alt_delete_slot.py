# Generated by Django 5.1 on 2025-07-13 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainers", "0013_slot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainerimage",
            name="alt",
            field=models.CharField(
                blank=True,
                default="Описание",
                max_length=255,
                null=True,
                verbose_name="Описание к фото",
            ),
        ),
        migrations.DeleteModel(
            name="Slot",
        ),
    ]
