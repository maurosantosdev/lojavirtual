# Generated by Django 3.0.5 on 2020-05-17 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_updateaddressuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UpdateAddressUser',
        ),
        migrations.AddField(
            model_name='user',
            name='bairro',
            field=models.CharField(default=1, max_length=100, verbose_name='Bairro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='complemento',
            field=models.CharField(default=1, max_length=200, verbose_name='Complemento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='numero',
            field=models.CharField(default=1, max_length=20, verbose_name='Número'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='rua',
            field=models.CharField(default=1, max_length=240, verbose_name='Rua'),
            preserve_default=False,
        ),
    ]
