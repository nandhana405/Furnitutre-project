# Generated by Django 4.2.16 on 2024-10-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Mail', models.EmailField(blank=True, max_length=100, null=True)),
                ('Mobile', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Pass1', models.CharField(blank=True, max_length=100, null=True)),
                ('Pass2', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
