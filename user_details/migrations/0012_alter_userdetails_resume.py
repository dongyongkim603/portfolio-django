# Generated by Django 4.2.4 on 2023-09-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0011_remove_userpost_resume_userdetails_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='resume',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]
