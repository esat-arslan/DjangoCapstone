# Generated by Django 5.1.1 on 2024-09-14 08:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=100)),
                ('roll_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999)])),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
