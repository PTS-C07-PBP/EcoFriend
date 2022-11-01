# Generated by Django 4.1 on 2022-10-20 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_author_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author_created',
            new_name='admin_created',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_id',
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]