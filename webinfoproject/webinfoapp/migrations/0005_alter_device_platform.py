# Generated by Django 4.2.6 on 2023-10-28 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webinfoapp', '0004_alter_device_options_alter_platform_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='platform',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='webinfoapp.platform'),
        ),
    ]
