# Generated by Django 4.1 on 2022-10-29 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_article_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
    ]
