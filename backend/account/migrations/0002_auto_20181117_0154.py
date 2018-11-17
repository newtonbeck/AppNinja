# Generated by Django 2.1.3 on 2018-11-17 01:54

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='etnia',
            field=models.IntegerField(choices=[(0, 'Negra'), (1, 'Indígena'), (2, 'Asiática'), (3, 'Caucasiana'), (4, 'Mestiça'), (5, 'Outra')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Masculino'), (1, 'Feminino'), (2, 'Prefiro não declarar')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ident_genero',
            field=models.IntegerField(choices=[(0, 'Cisgênero'), (1, 'Transgênero'), (2, 'Neutro ou Não-binario'), (3, 'Prefiro não declarar')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='orient_sex',
            field=models.IntegerField(choices=[(0, 'Heterossexual'), (1, 'Homossexual'), (2, 'Bissexual'), (3, 'Pansexual'), (4, 'Assexual'), (5, 'Fluido'), (6, 'Prefiro não declarar')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
