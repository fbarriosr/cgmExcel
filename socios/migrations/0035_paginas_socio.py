# Generated by Django 3.1.7 on 2024-04-10 15:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0034_auto_20240410_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paginas_Socio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='Paginas_Socio/')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(default=0)),
                ('file', models.FileField(blank=True, max_length=254, upload_to='Paginas_Socio/files/')),
            ],
            options={
                'verbose_name': 'Paginas_Socio',
                'verbose_name_plural': 'Paginas_Socios',
                'ordering': ['order'],
            },
        ),
    ]
