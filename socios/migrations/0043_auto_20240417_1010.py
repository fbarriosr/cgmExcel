# Generated by Django 3.1.7 on 2024-04-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0042_auto_20240417_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='auto',
            field=models.BooleanField(default=False, verbose_name='Estacionamiento'),
        ),
    ]
