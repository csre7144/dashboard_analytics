# Generated by Django 5.0.4 on 2024-08-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
