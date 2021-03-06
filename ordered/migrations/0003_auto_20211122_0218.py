# Generated by Django 3.2.9 on 2021-11-22 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordered', '0002_menuorderedline'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkorderedline',
            name='ordered',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ordered.ordered'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mealorderedline',
            name='ordered',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ordered.ordered'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuorderedline',
            name='ordered',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ordered.ordered'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wineorderedline',
            name='ordered',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ordered.ordered'),
            preserve_default=False,
        ),
    ]
