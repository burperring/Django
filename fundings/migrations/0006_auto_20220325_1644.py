# Generated by Django 2.2.5 on 2022-03-25 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fundings', '0005_auto_20220325_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='amenities',
            field=models.ManyToManyField(blank=True, related_name='fundings', to='fundings.Amenity'),
        ),
        migrations.AlterField(
            model_name='funding',
            name='facilities',
            field=models.ManyToManyField(blank=True, related_name='fundings', to='fundings.Facility'),
        ),
        migrations.AlterField(
            model_name='funding',
            name='house_rules',
            field=models.ManyToManyField(blank=True, related_name='fundings', to='fundings.HouseRule'),
        ),
        migrations.AlterField(
            model_name='funding',
            name='music_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='music_types', to='fundings.MusicType'),
        ),
    ]
