# Generated by Django 3.2.9 on 2022-01-26 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0004_auto_20220123_1957'),
        ('drink', '0012_alter_drink_sale_price_ml'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='restuarant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employe.restaurant'),
            preserve_default=False,
        ),
    ]
