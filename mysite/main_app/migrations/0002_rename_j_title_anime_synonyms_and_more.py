# Generated by Django 4.0.5 on 2022-08-26 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='j_title',
            new_name='synonyms',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='j_name',
            new_name='synonyms',
        ),
        migrations.RenameField(
            model_name='manga',
            old_name='j_title',
            new_name='synonyms',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='j_name',
            new_name='synonyms',
        ),
    ]
