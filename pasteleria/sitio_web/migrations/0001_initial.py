# Generated by Django 3.1.2 on 2020-10-28 01:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido_cabecera',
            fields=[
                ('numero_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('hora_creacion', models.TimeField()),
                ('fecha_entrega', models.DateField()),
                ('hora_entrega', models.TimeField()),
                ('rut_cliente', models.CharField(max_length=10)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('telefono_cliente', models.IntegerField()),
                ('email_cliente', models.EmailField(max_length=254)),
                ('direccion_entrega', models.CharField(max_length=200)),
                ('valor_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('valor', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido_posicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('valor_posicion', models.IntegerField()),
                ('codigo_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio_web.producto')),
                ('numero_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio_web.pedido_cabecera')),
            ],
        ),
    ]