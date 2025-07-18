# Generated by Django 5.1 on 2025-07-14 13:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_delete_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name='Дата создания'
            ),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='updated_at',
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name='Дата обновления',
            ),
        ),
    ]
