# Generated by Django 5.0.1 on 2024-02-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Traders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=80)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=150)),
            ],
        ),
    ]
