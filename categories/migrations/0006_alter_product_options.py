# Generated by Django 5.0.4 on 2024-08-02 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_rename_subcategory_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product'},
        ),
    ]
