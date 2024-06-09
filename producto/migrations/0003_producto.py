# Generated by Django 5.0.6 on 2024-06-09 18:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_alter_productocategoria_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('unidad_de_medida', models.CharField(max_length=200)),
                ('cantidad', models.FloatField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('fecha_actualizacion', models.DateField(blank=True, default=django.utils.timezone.now, editable=False, null=True)),
                ('categoria_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.productocategoria')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]
