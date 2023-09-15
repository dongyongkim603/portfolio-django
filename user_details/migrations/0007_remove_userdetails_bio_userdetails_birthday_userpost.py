# Generated by Django 4.2.4 on 2023-09-15 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_details', '0006_alter_userdetails_profile_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='bio',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('description', models.TextField()),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('creator_details', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_details.userdetails')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]