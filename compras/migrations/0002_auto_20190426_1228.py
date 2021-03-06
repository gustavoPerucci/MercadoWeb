# Generated by Django 2.1.5 on 2019-04-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='status_compra',
            field=models.CharField(default='NAO LANCADO', max_length=30),
        ),
        migrations.AlterField(
            model_name='compras',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=15),
        ),
        migrations.AlterField(
            model_name='entradaprodutos',
            name='balanco',
            field=models.CharField(default='ABERTO', max_length=20),
        ),
        migrations.AlterField(
            model_name='entradaprodutos',
            name='numero_lote',
            field=models.CharField(blank=True, default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='entradaprodutos',
            name='preco_compra',
            field=models.DecimalField(decimal_places=3, default='0', max_digits=15),
        ),
        migrations.AlterField(
            model_name='entradaprodutos',
            name='status_entrada',
            field=models.CharField(default='LANCADO', max_length=15),
        ),
        migrations.AlterField(
            model_name='entradaprodutos',
            name='total',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=15),
        ),
    ]
