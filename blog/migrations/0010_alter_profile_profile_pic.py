# Generated by Django 4.1.5 on 2023-01-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]