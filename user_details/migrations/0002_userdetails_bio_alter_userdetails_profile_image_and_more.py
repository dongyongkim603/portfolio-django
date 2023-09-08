# Generated by Django 4.2.4 on 2023-09-08 14:20

from django.db import migrations, models
import user_details.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=user_details.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=user_details.models.user_directory_path),
        ),
    ]
