# Generated by Django 4.0.5 on 2022-08-31 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_manga_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='episodes_now',
            field=models.IntegerField(default=0, verbose_name='Episodes now'),
        ),
    ]