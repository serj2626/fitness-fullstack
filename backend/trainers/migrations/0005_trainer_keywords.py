# Generated by Django 5.1 on 2025-06-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainers", "0004_trainer_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainer",
            name="keywords",
            field=models.CharField(
                blank=True,
                help_text="Через запятую",
                max_length=255,
                null=True,
                verbose_name="Ключевые слова",
            ),
        ),
    ]
