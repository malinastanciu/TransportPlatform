# Generated by Django 4.0 on 2022-01-12 10:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_request_email_request_other_details_request_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='registration_date',
        ),
        migrations.AddField(
            model_name='offer',
            name='arrival_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 10, 50, 40, 377735, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='offer',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 10, 50, 40, 377735, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='offer',
            name='destination',
            field=models.CharField(default='a', max_length=30),
        ),
        migrations.AddField(
            model_name='offer',
            name='email',
            field=models.CharField(default='a', max_length=50),
        ),
        migrations.AddField(
            model_name='offer',
            name='other_details',
            field=models.CharField(default='a', max_length=200),
        ),
        migrations.AddField(
            model_name='offer',
            name='phone',
            field=models.CharField(default='0', max_length=11),
        ),
        migrations.AddField(
            model_name='offer',
            name='price_per_km_emptyTruck',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='offer',
            name='source',
            field=models.CharField(default='a', max_length=30),
        ),
        migrations.AddField(
            model_name='request',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 10, 50, 59, 569219, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='price_per_km',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='request',
            name='arrival_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 10, 50, 40, 376739, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request',
            name='max_price',
            field=models.FloatField(default=0),
        ),
    ]