# Generated by Django 3.0.1 on 2019-12-29 04:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    atomic= False
    dependencies = [
        ('contact', '0002_auto_20191229_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='date_send',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
