# Generated by Django 2.2.5 on 2022-06-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0010_auto_20220607_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
