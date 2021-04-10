# Generated by Django 3.0.1 on 2019-12-31 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    atomic = False
    dependencies = [
        ('projects', '0004_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, default='media/project_image/NO_IMAGE.jpg', height_field='height_field', null=True, upload_to='project_image', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
