# Generated by Django 2.2.5 on 2022-03-29 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0003_auto_20220326_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='music_type',
        ),
        migrations.DeleteModel(
            name='MusicType',
        ),
    ]