# Generated by Django 3.2.9 on 2021-11-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='price',
        ),
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default='', help_text='Ex:Coca', max_length=150, unique=True, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='discount',
            field=models.DecimalField(decimal_places=2, help_text='Ex: 30', max_digits=11, max_length=255, verbose_name='Discount(%)'),
        ),
    ]
