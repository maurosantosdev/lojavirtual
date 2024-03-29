# Generated by Django 3.0.5 on 2020-05-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NovidadeEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'Novidade E-mail',
                'verbose_name_plural': 'Novidades E-mail',
                'ordering': ['email'],
            },
        ),
    ]
