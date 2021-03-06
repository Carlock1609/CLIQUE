# Generated by Django 3.0.2 on 2020-01-18 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200117_1719'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhotoLibrary',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cover_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile/profile_backgrounds/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile/profile_images/'),
        ),
    ]
