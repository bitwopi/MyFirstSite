# Generated by Django 4.0.5 on 2022-08-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_person_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='career',
            field=models.ManyToManyField(to='main_app.career', verbose_name='Career'),
        ),
    ]
