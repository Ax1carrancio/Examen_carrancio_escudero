# Generated by Django 4.0.5 on 2022-07-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jardinesapp', '0006_producto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['id'], 'verbose_name': 'Producto'},
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_pro',
            field=models.CharField(max_length=40, verbose_name='Nombre del Producto'),
        ),
        migrations.AlterModelTable(
            name='producto',
            table='producto',
        ),
    ]
