# Generated by Django 3.2.5 on 2022-01-18 12:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='arrival_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 18, 12, 59, 26, 930737, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 18, 12, 59, 26, 930737, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request',
            name='arrival_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 18, 12, 59, 26, 930737, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 18, 12, 59, 26, 930737, tzinfo=utc)),
        ),
    ]