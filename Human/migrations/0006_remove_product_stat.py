# Generated by Django 3.0.5 on 2020-04-10 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Human', '0005_auto_20200410_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stat',
        ),
    ]
