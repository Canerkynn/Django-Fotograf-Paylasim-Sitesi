# Generated by Django 3.0.5 on 2020-05-09 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        ('Human', '0016_auto_20200507_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='content.Content'),
            preserve_default=False,
        ),
    ]
