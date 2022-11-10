# Generated by Django 2.2.3 on 2022-11-10 09:20

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
                ('nombre_M', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_P', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('detalles', models.CharField(max_length=20)),
                ('nombre_M', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.Marca')),
            ],
        ),
    ]
