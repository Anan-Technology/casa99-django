# Generated by Django 3.0.1 on 2019-12-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
