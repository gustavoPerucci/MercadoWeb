# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-19 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaResponsaveis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('observacoes', models.TextField(blank=True, max_length=250)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('empresa',),
                'db_table': 'empresas_responsaveis',
            },
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('razao_social', models.CharField(blank=True, max_length=50, unique=True, verbose_name=b'Raz\xc3\xa3o social')),
                ('nome_fantasia', models.CharField(max_length=50, unique=True, verbose_name=b'Nome Fantasia')),
                ('cnpj', models.CharField(blank=True, max_length=20, verbose_name=b'Cnpj')),
                ('inscricao_estadual', models.CharField(blank=True, max_length=20, verbose_name=b'Inscri\xc3\xa7\xc3\xa3o estadual')),
                ('inscricao_municipal', models.CharField(blank=True, max_length=20, verbose_name=b'Inscri\xc3\xa7\xc3\xa3o municipal')),
                ('contato', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=30)),
                ('celular', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name=b'E-mail')),
                ('site', models.CharField(max_length=50)),
                ('cep', models.CharField(blank=True, max_length=9)),
                ('endereco', models.CharField(max_length=40)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=30)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('contato_cobranca', models.CharField(blank=True, max_length=30)),
                ('telefone_cobranca', models.CharField(blank=True, max_length=30)),
                ('celular_cobranca', models.CharField(blank=True, max_length=30)),
                ('email_cobranca', models.EmailField(max_length=254, verbose_name=b'E-mail cobran\xc3\xa7a')),
                ('cep_cobranca', models.CharField(blank=True, max_length=9)),
                ('endereco_cobranca', models.CharField(blank=True, max_length=40)),
                ('numero_cobranca', models.CharField(blank=True, max_length=10)),
                ('complemento_cobranca', models.CharField(blank=True, max_length=30)),
                ('bairro_cobranca', models.CharField(blank=True, max_length=50)),
                ('cidade_cobranca', models.CharField(blank=True, max_length=50)),
                ('uf_cobranca', models.CharField(blank=True, max_length=2)),
                ('dia_pagamento', models.IntegerField(blank=True, null=True)),
                ('desconto', models.DecimalField(decimal_places=2, default=b'0', max_digits=4, verbose_name=b'Percentual desconto %')),
                ('forma_pagamento', models.CharField(choices=[(b'A VISTA', b'A VISTA'), (b'PARCELADO', b'PARCELADO'), (b'GRATUIDADE', b'GRATUIDADE')], max_length=20, verbose_name=b'Forma pagamento')),
                ('meio_pagamento', models.CharField(choices=[(b'BOLETO BANCARIO', b'BOLETO BANCARIO'), (b'DINHEIRO EM ESPECIE', b'DINHEIRO EM ESPECIE'), (b'DEPOSITO EM CONTA', b'DEPOSITO EM CONTA'), (b'CARTAO DE CREDITO', b'CARTAO DE CREDITO'), (b'CARTAO DE DEBITO', b'CARTAO DE DEBITO'), (b'DEBITO EM CONTA', b'DEBITO EM CONTA'), (b'GRATUIDADE', b'GRATUIDADE'), (b'OUTROS', b'OUTROS')], max_length=20, verbose_name=b'Meio de pagamento')),
                ('status', models.CharField(choices=[(b'ATIVO', b'ATIVO'), (b'INATIVO', b'INATIVO'), (b'SUSPENSO', b'SUSPENSO'), (b'EXCLUIDO', b'EXCLUIDO'), (b'NEGATIVADO', b'NEGATIVADO')], max_length=20, verbose_name=b'St\xc3\xa1tus')),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('contrato', models.CharField(blank=True, max_length=30, verbose_name=b'Contrato')),
                ('observacoes', models.TextField(blank=True, max_length=250)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('nome_fantasia',),
                'db_table': 'empresas',
            },
        ),
        migrations.CreateModel(
            name='Planos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True, verbose_name=b'Nome do plano')),
                ('descricao', models.TextField(blank=True, max_length=100, verbose_name=b'Descricao do plano')),
                ('valor', models.DecimalField(decimal_places=2, default=b'0', max_digits=15, verbose_name=b'Valor')),
                ('desconto_maximo', models.DecimalField(decimal_places=2, default=b'0', max_digits=15, verbose_name=b'Desconto m\xc3\xa1ximo %')),
                ('observacoes', models.TextField(blank=True, max_length=250, verbose_name=b'Observa\xc3\xa7\xc3\xb5es')),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ('nome',),
                'db_table': 'planos',
            },
        ),
        migrations.AddField(
            model_name='empresas',
            name='plano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.Planos'),
        ),
        migrations.AddField(
            model_name='empresaresponsaveis',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empresas.Empresas'),
        ),
        migrations.AddField(
            model_name='empresaresponsaveis',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
