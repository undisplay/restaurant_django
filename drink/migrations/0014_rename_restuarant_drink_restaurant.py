# Generated by Django 3.2.9 on 2022-01-27 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0013_drink_restuarant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drink',
            old_name='restuarant',
            new_name='restaurant',
        ),
    ]