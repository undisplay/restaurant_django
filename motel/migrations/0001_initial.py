# Generated by Django 3.2.9 on 2022-01-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('loan_price', models.DecimalField(decimal_places=2, help_text='Ex: 300', max_digits=11, max_length=255, verbose_name='Price')),
                ('number', models.CharField(help_text='Ex: CH1', max_length=255, verbose_name='Number')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='entry date')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]