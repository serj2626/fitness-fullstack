# Generated by Django 5.1 on 2025-07-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0002_alter_post_created_at_alter_post_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='Дата создания'
            ),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='Дата обновления'
            ),
        ),
    ]
