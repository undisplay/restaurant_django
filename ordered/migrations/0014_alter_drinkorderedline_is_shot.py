# Generated by Django 3.2.9 on 2022-01-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordered', '0013_rename_is_ml_drinkorderedline_is_shot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkorderedline',
            name='is_shot',
            field=models.BooleanField(default=False, verbose_name='Is shot'),
        ),
    ]
