# Generated by Django 3.0.5 on 2020-05-05 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Human', '0012_auto_20200502_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]