# Generated by Django 4.2.2 on 2025-03-30 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('treats', 'treats'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
