# Generated by Django 5.0.4 on 2024-08-02 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0009_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product category', 'verbose_name_plural': 'product'},
        ),
    ]
