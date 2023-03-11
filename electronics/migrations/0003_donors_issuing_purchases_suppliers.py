# Generated by Django 4.1.6 on 2023-02-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0002_alter_procurements_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=2555)),
                ('email', models.EmailField(max_length=254)),
                ('Items_supplied', models.CharField(max_length=2555)),
                ('quantity', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Issuing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=2555)),
                ('Issued_to', models.CharField(max_length=255)),
                ('Quantity', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=2555)),
                ('Quantity', models.CharField(max_length=2555)),
                ('Price', models.CharField(max_length=255)),
                ('Supplier', models.CharField(max_length=2555)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=2555)),
                ('email', models.EmailField(max_length=254)),
                ('Items_supplied', models.CharField(max_length=2555)),
                ('quantity', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
    ]
