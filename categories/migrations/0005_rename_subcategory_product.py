# Generated by Django 5.0.4 on 2024-08-02 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_subcategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='subcategory',
            new_name='product',
        ),
    ]
