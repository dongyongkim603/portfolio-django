# Generated by Django 4.2.4 on 2023-09-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0010_userpost_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='resume',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='resume',
            field=models.FileField(blank=True, null=True, unique=True, upload_to=''),
        ),
    ]