# Generated by Django 4.0.2 on 2022-09-30 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BirdCounter', '0004_rename_eagles_eagle'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('name', models.CharField(max_length=1000, unique=True)),
                ('id', models.CharField(max_length=1000, primary_key=True, serialize=False, unique=True)),
                ('region', models.CharField(max_length=1000)),
            ],
        ),
    ]
