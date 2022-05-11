# Generated by Django 2.2.5 on 2022-05-11 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0007_auto_20220412_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('sfile', models.FileField(upload_to='musics/')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='musics.Music')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]