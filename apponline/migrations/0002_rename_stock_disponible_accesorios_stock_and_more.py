# Generated by Django 4.1.1 on 2022-09-06 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apponline', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesorios',
            old_name='stock_disponible',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='camperas',
            old_name='stock_disponible',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='carteras',
            old_name='stock_disponible',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='zapatos',
            old_name='stock_disponible',
            new_name='stock',
        ),
    ]
