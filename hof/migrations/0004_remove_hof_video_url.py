# Generated by Django 3.2 on 2022-02-13 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hof', '0003_hof_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hof',
            name='video_url',
        ),
    ]
