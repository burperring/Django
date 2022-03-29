# Generated by Django 2.2.5 on 2022-03-29 07:24

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fundings', '0008_auto_20220326_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='baths',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='funding',
            name='bedrooms',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='funding',
            name='beds',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='funding',
            name='country',
            field=django_countries.fields.CountryField(default='korea', max_length=2),
        ),
        migrations.AlterField(
            model_name='funding',
            name='guests',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='funding',
            name='price',
            field=models.IntegerField(default=5),
        ),
    ]