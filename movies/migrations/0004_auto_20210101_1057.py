# Generated by Django 3.1.4 on 2021-01-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210101_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='dailyRentalRate',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='numberInStock',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]