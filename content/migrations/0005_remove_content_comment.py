# Generated by Django 3.0.5 on 2020-05-14 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_content_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='comment',
        ),
    ]
