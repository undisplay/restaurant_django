# Generated by Django 3.2.9 on 2022-01-27 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motel', '0003_room_restuarant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='restuarant',
            new_name='restaurant',
        ),
    ]