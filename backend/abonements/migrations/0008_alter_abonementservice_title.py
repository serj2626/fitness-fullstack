# Generated by Django 5.1 on 2025-07-18 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonements', '0007_alter_orderabonement_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonementservice',
            name='title',
            field=models.CharField(
                choices=[
                    ('gym', 'Тренажерный зал'),
                    ('pool', 'Бассейн'),
                    ('yoga', 'Йога'),
                    ('spa', 'SPA'),
                    ('cosmetology', 'Косметология'),
                    ('cycle', 'Велотренажер'),
                    ('water aerobics', 'Водное аэробик'),
                    ('dancing', 'Танцы'),
                    ('group', 'Групповые занятия'),
                ],
                max_length=100,
                verbose_name='Название',
            ),
        ),
    ]
