# Generated by Django 3.2.9 on 2021-11-18 04:34

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ex:Coca', max_length=150, unique=True, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, help_text='Ex: 300', max_digits=11, max_length=255, verbose_name='Price')),
                ('sale_price', models.DecimalField(decimal_places=2, help_text='Ex: 30', max_digits=11, max_length=255, verbose_name='Sale Price')),
                ('type', models.CharField(help_text='Ex:Main', max_length=150, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Winegrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Ex:+509XXXXXXXX', max_length=15, region=None, verbose_name='Phone')),
                ('address', models.TextField(blank=True, help_text='Entrer address', null=True, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='')),
                ('price', models.DecimalField(decimal_places=2, help_text='Ex: 300', max_digits=11, max_length=255, verbose_name='Price')),
                ('sale_price', models.DecimalField(decimal_places=2, help_text='Ex: 30', max_digits=11, max_length=255, verbose_name='Sale Price')),
                ('buy_date', models.DateField(auto_now_add=True, verbose_name='Buy date')),
                ('winegrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.winegrower')),
            ],
        ),
    ]