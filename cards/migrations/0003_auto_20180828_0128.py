# Generated by Django 2.1 on 2018-08-28 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20180828_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cardType',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(max_length=32),
        ),
    ]