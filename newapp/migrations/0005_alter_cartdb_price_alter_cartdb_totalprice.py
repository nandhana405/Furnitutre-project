# Generated by Django 4.2.16 on 2024-11-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_cartdb_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdb',
            name='price',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cartdb',
            name='totalprice',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
