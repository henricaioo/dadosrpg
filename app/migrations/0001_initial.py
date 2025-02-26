# Generated by Django 5.1.5 on 2025-01-29 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atributo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome do atributo')),
                ('abreviacao', models.CharField(max_length=3, verbose_name='Abreviação do atributo')),
                ('descricao', models.TextField(verbose_name='Descrição do atributo')),
            ],
            options={
                'verbose_name': 'Atributo',
                'verbose_name_plural': 'Atributos',
            },
        ),
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome da campanha')),
                ('descricao', models.TextField(verbose_name='História/descrição da campanha')),
            ],
            options={
                'verbose_name': 'Campanha',
                'verbose_name_plural': 'Campanhas',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome do item')),
                ('descricao', models.TextField(verbose_name='Descrição do item')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
            },
        ),
        migrations.CreateModel(
            name='Pericia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome da perícia')),
                ('descricao', models.TextField(verbose_name='Descrição da perícia')),
            ],
            options={
                'verbose_name': 'Perícia',
                'verbose_name_plural': 'Perícias',
            },
        ),
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome do personagem')),
                ('aparencia', models.TextField(verbose_name='Aparência do personagem')),
                ('historia', models.TextField(verbose_name='Nome do personagem')),
                ('vida', models.CharField(max_length=20, verbose_name='Nome do personagem')),
            ],
            options={
                'verbose_name': 'Personagem',
                'verbose_name_plural': 'Personagens',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome da pessoa')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='PersonagemAtributo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(verbose_name='Valor')),
                ('atributo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.atributo', verbose_name='Atributo')),
                ('personagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.personagem', verbose_name='Personagem que possui a preícia')),
            ],
            options={
                'verbose_name': 'Atributo',
                'verbose_name_plural': 'Atributos',
            },
        ),
        migrations.CreateModel(
            name='PersonagemCampanha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campanha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.campanha', verbose_name='Campanha')),
                ('personagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.personagem', verbose_name='Personagem na camapanha')),
            ],
        ),
        migrations.CreateModel(
            name='PersonagemItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtde', models.IntegerField(verbose_name='Quantidade')),
                ('durabilidade', models.CharField(max_length=20, verbose_name='Quantidade')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item', verbose_name='Item')),
                ('personagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.personagem', verbose_name='Personagem que possui o item')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
            },
        ),
        migrations.CreateModel(
            name='PersonagemPericia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(verbose_name='Valor')),
                ('pericia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pericia', verbose_name='Perícia')),
                ('personagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.personagem', verbose_name='Personagem que possui a preícia')),
            ],
            options={
                'verbose_name': 'Perícia',
                'verbose_name_plural': 'Perícias',
            },
        ),
        migrations.AddField(
            model_name='personagem',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Dono do personagem'),
        ),
        migrations.AddField(
            model_name='campanha',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Dono da camapanha'),
        ),
    ]
