# Generated by Django 2.2.5 on 2022-04-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundings', '0010_auto_20220329_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='funding_photos'),
        ),
    ]
