# Generated by Django 4.0.5 on 2022-08-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_anime_duration_alter_anime_episodes_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='rate',
            field=models.FloatField(default=0, verbose_name='Rating'),
        ),
    ]
