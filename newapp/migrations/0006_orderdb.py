# Generated by Django 4.2.16 on 2024-11-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_alter_cartdb_price_alter_cartdb_totalprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('mail', models.EmailField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(blank=True, max_length=100, null=True)),
                ('total_price', models.IntegerField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
