# Generated by Django 2.0.5 on 2018-05-25 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='study_sort',
            old_name='study_tag2',
            new_name='study_tag_three',
        ),
        migrations.RenameField(
            model_name='study_sort',
            old_name='study_tag1',
            new_name='study_tag_two',
        ),
    ]
