# Generated by Django 3.2.9 on 2021-11-22 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0002_auto_20211121_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='creation_date',
            field=models.DateField(auto_now_add=True, verbose_name='creation_date'),
        ),
    ]
