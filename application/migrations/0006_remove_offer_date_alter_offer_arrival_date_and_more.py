# Generated by Django 4.0 on 2022-01-12 10:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_offer_arrival_date_alter_offer_departure_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='date',
        ),
        migrations.AlterField(
            model_name='offer',
            name='arrival_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 10, 54, 5, 995162, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 10, 54, 5, 994331, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request',
            name='arrival_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 10, 54, 5, 993220, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 10, 54, 5, 993220, tzinfo=utc)),
        ),
    ]
