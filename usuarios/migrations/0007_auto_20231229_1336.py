# Generated by Django 3.1.7 on 2023-12-29 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20231229_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=12, unique=True, verbose_name='Rut'),
        ),
    ]
