# Generated by Django 4.2.16 on 2024-11-03 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_proveedor_product_proveedor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proveedor',
            new_name='Supplier',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='proveedor',
            new_name='supplier',
        ),
    ]