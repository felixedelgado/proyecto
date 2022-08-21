# Generated by Django 4.1 on 2022-08-21 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Nombre del evento')),
                ('date', models.DateTimeField(verbose_name='Dia del evento')),
                ('descripcion', models.TextField(blank=True, max_length=150)),
                ('lugar', models.CharField(max_length=70)),
            ],
        ),
    ]
