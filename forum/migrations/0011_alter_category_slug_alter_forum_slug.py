# Generated by Django 4.2.4 on 2023-09-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_alter_forum_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
