# Generated by Django 3.2.8 on 2022-01-27 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socio',
            name='personal',
        ),
    ]
