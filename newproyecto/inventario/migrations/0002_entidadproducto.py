# Generated by Django 4.2.3 on 2023-07-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidadproducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('siglas', models.CharField(max_length=30)),
                ('numero_producto', models.IntegerField()),
                ('detalle', models.CharField(max_length=100)),
            ],
        ),
    ]
