# Generated by Django 5.1.2 on 2024-10-15 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='description',
        ),
    ]