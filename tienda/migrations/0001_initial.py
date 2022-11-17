# Generated by Django 4.1.3 on 2022-11-17 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('nombre_M', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre_P', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('unidades', models.IntegerField(verbose_name='Unidades')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('detalles', models.CharField(max_length=30)),
                ('nombre_M', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tienda.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Vendido',
            fields=[
                ('id_compra', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id_Compra')),
                ('id_cliente', models.IntegerField(verbose_name='Id_Cliente')),
                ('unidades', models.IntegerField(verbose_name='Unidades')),
                ('importe', models.FloatField(verbose_name='Importe')),
                ('nombre_M', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tienda.marca')),
                ('nombre_P', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tienda.producto')),
            ],
        ),
    ]
