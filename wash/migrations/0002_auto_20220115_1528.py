# Generated by Django 3.2.9 on 2022-01-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wash',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/images/'),
        ),
        migrations.AddField(
            model_name='wash',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='wash',
            name='type',
            field=models.CharField(help_text='Ex:Car', max_length=255, verbose_name='Type'),
        ),
    ]
