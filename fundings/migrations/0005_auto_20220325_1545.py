# Generated by Django 2.2.5 on 2022-03-25 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fundings', '0004_auto_20220317_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fundings', to=settings.AUTH_USER_MODEL),
        ),
    ]
