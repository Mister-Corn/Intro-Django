# Generated by Django 2.1 on 2018-08-28 01:30

import cards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20180828_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cardType',
            field=models.CharField(choices=[(cards.models.TypeChoice('sorcery'), 'sorcery'), (cards.models.TypeChoice('instant'), 'instant'), (cards.models.TypeChoice('land'), 'land'), (cards.models.TypeChoice('creature'), 'creature')], max_length=128),
        ),
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[(cards.models.ColorChoice('white'), 'white'), (cards.models.ColorChoice('black'), 'black'), (cards.models.ColorChoice('red'), 'red'), (cards.models.ColorChoice('green'), 'green'), (cards.models.ColorChoice('blue'), 'blue')], max_length=32),
        ),
    ]
