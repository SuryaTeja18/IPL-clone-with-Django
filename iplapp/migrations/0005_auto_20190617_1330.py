# Generated by Django 2.2.1 on 2019-06-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplapp', '0004_auto_20190617_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveries',
            name='bat_team',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='bowl_team',
            field=models.CharField(max_length=128),
        ),
    ]
