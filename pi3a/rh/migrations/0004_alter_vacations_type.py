# Generated by Django 3.2.18 on 2023-04-14 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0003_auto_20230413_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacations',
            name='type',
            field=models.CharField(default='ferias', max_length=50),
        ),
    ]