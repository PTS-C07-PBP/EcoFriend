# Generated by Django 4.1 on 2022-10-27 19:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_alter_footprint_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footprint',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]