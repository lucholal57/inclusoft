# Generated by Django 3.2.8 on 2021-12-31 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0023_taller_alumno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taller',
            name='alumno',
        ),
    ]
