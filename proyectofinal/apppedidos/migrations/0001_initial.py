# Generated by Django 2.2.3 on 2022-08-21 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apptienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'Pedidos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='LineaPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pedido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apppedidos.Pedidos')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptienda.Producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'linea pedido',
                'verbose_name_plural': 'linea pedidos',
                'db_table': 'LineaPedidos',
                'ordering': ['id'],
            },
        ),
    ]
