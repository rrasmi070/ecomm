# Generated by Django 3.1.5 on 2021-01-22 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20210122_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproduct',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Cartproduct',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
