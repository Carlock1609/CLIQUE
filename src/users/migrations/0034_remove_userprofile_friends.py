# Generated by Django 3.0.2 on 2020-02-04 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_auto_20200202_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friends',
        ),
    ]
