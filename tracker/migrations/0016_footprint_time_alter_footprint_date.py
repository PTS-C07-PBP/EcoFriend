# Generated by Django 4.1 on 2022-10-28 01:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0015_alter_footprint_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='footprint',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='footprint',
            name='date',
            field=models.DateField(),
        ),
    ]
