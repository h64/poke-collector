# Generated by Django 2.1.2 on 2018-10-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20181015_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokedexpokemon',
            name='pokedex_id',
            field=models.CharField(max_length=5),
        ),
    ]