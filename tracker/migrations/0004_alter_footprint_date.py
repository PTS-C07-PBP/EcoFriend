# Generated by Django 4.1 on 2022-10-27 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_footprint_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footprint',
            name='date',
            field=models.DateTimeField(default='27.10.2022 10:03:34'),
        ),
    ]
