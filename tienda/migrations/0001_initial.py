# Generated by Django 4.1.3 on 2022-11-11 11:30

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_P', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('unidades', models.IntegerField(verbose_name='Unidades')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('detalles', models.CharField(max_length=30)),
                ('nombre_M', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tienda.marca')),
            ],
        ),
    ]
