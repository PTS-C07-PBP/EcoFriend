# Generated by Django 4.1 on 2022-10-28 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comments',
            new_name='description',
        ),
    ]
