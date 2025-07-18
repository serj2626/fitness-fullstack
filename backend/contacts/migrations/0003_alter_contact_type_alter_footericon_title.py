# Generated by Django 5.1 on 2025-06-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0002_footericon_footer_footerlink_footer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="type",
            field=models.CharField(
                choices=[
                    ("phone", "Телефон"),
                    ("mail", "Почта"),
                    ("address", "Адрес"),
                    ("mode", "Режим работы"),
                    ("latitude", "Широта"),
                    ("longitude", "Долгота"),
                ],
                default="phone",
                max_length=50,
                unique=True,
                verbose_name="Тип",
            ),
        ),
        migrations.AlterField(
            model_name="footericon",
            name="title",
            field=models.CharField(
                choices=[
                    ("vk", "Вконтакте"),
                    ("telegram", "Телеграм"),
                    ("whatsapp", "Ватсап"),
                    ("linkedin", "Linkedin"),
                ],
                max_length=255,
                unique=True,
                verbose_name="Название",
            ),
        ),
    ]
