# Generated by Django 2.2.5 on 2022-04-12 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundings', '0015_auto_20220412_1231'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Amenity',
        ),
        migrations.DeleteModel(
            name='Facility',
        ),
        migrations.DeleteModel(
            name='HouseRule',
        ),
    ]
