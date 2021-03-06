# Generated by Django 2.1.5 on 2019-04-26 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saidaprodutos',
            name='balanco',
            field=models.CharField(choices=[('ABERTO', 'ABERTO'), ('FECHADO', 'FECHADO')], default='ABERTO', max_length=20, verbose_name='Balanço'),
        ),
        migrations.AlterField(
            model_name='saidaprodutos',
            name='observacoes_saida',
            field=models.TextField(blank=True, max_length=200, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='saidaprodutos',
            name='percentual_desconto',
            field=models.DecimalField(decimal_places=3, default='0', max_digits=15, verbose_name='Desconto %'),
        ),
        migrations.AlterField(
            model_name='saidaprodutos',
            name='quantidade',
            field=models.DecimalField(decimal_places=3, max_digits=15, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='saidaprodutos',
            name='saldo_final',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=15),
        ),
        migrations.AlterField(
            model_name='saidaprodutos',
            name='status',
            field=models.CharField(choices=[('EM SEPARACAO', 'EM SEPARACAO'), ('SEPARADO', 'SEPARADO'), ('ENTREGUE', 'ENTREGUE'), ('CANCELADO', 'CANCELADO')], default='AGUARDANDO', max_length=20, verbose_name='Státus'),
        ),
        migrations.AlterField(
            model_name='saidaprodutos',
            name='total_desconto',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Desconto total'),
        ),
        migrations.AlterField(
            model_name='saidaprodutos',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Valor total'),
        ),
        migrations.AlterField(
            model_name='saidaprodutos',
            name='valor_unitario',
            field=models.DecimalField(decimal_places=3, default='0', max_digits=15, verbose_name='Valor unitário'),
        ),
        migrations.AlterField(
            model_name='saidaprodutos',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.Vendas', verbose_name='Nome/Razão social:'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='bairro',
            field=models.CharField(blank=True, max_length=50, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='cep',
            field=models.CharField(blank=True, max_length=10, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='cidade',
            field=models.CharField(blank=True, max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='desconto',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Desconto'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='endereco',
            field=models.CharField(blank=True, max_length=50, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='estado',
            field=models.CharField(blank=True, max_length=2, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='observacoes',
            field=models.TextField(blank=True, max_length=200, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='observacoes_entrega',
            field=models.TextField(blank=True, max_length=200, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='saldo_final',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Saldo final'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='solicitante',
            field=models.CharField(max_length=50, verbose_name='Solicitante'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='status_pedido',
            field=models.CharField(default='EM ANDAMENTO', max_length=30, verbose_name='Státus do Pedido'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Valor total'),
        ),
    ]
