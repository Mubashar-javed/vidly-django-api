# Generated by Django 3.1.4 on 2020-12-31 07:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Genre Name'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=250, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]