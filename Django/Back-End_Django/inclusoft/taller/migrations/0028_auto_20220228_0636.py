# Generated by Django 3.2.8 on 2022-02-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0027_auto_20220102_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras_taller',
            name='cantidad',
            field=models.CharField(default=20, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compras_taller',
            name='fecha_compra',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='compras_taller',
            name='precio',
            field=models.CharField(default=20, max_length=10),
            preserve_default=False,
        ),
    ]
