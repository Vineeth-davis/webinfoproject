# Generated by Django 4.2.6 on 2023-10-27 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webinfoapp', '0002_user_technician_administrator'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
