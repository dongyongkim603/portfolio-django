# Generated by Django 4.2.4 on 2023-08-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_alter_comment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]