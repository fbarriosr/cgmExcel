# Generated by Django 3.1.7 on 2024-01-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20231229_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email'),
        ),
    ]
