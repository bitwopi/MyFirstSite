# Generated by Django 4.0.5 on 2022-08-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_anime_synonyms_alter_character_synonyms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='duration',
            field=models.DurationField(null=True, verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='episodes_now',
            field=models.IntegerField(null=True, verbose_name='Episodes now'),
        ),
    ]
