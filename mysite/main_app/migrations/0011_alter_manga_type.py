# Generated by Django 4.0.5 on 2022-08-30 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_manga_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main_app.type', verbose_name='Type'),
        ),
    ]
