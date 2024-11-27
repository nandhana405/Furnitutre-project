# Generated by Django 4.2.16 on 2024-10-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FApp', '0002_alter_category_db_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('mrp', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('manufactured', models.CharField(blank=True, max_length=100, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='Product')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='Product')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='Product')),
            ],
        ),
    ]