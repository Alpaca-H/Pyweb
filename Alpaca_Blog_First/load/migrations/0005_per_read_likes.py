# Generated by Django 2.0.5 on 2018-05-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0004_auto_20180515_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='per_read',
            name='likes',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='喜欢'),
        ),
    ]
