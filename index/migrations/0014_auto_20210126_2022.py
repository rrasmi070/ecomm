# Generated by Django 3.1.5 on 2021-01-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20210126_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('Order Confirm', 'Order Confirm'), ('Order received', 'Order received'), ('Order Processing', 'Order Processing'), ('Order On The Way', 'Order On The Way'), ('Order Conpleated', 'Order Conpleated'), ('Order Canceled', 'Order Canceled')], max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='shiping_address',
            field=models.TextField(),
        ),
    ]