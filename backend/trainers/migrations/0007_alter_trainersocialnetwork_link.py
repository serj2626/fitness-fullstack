# Generated by Django 5.1 on 2025-06-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainers", "0006_alter_trainer_keywords"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainersocialnetwork",
            name="link",
            field=models.CharField(max_length=56, verbose_name="Ссылка"),
        ),
    ]
