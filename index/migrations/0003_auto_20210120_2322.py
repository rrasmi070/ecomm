# Generated by Django 3.1.5 on 2021-01-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20210120_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men Fashion', 'Men Fashion'), ('Women Fashion', 'Women Fashion'), ('Gagets', 'Gagets'), ('Electronics', 'Electronics')], max_length=50),
        ),
    ]
