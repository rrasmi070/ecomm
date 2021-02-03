# Generated by Django 3.1.5 on 2021-01-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_delete_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='carousel')),
            ],
        ),
    ]