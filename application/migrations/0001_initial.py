# Generated by Django 4.0 on 2022-01-11 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('registration_plate', models.CharField(max_length=15, unique=True)),
                ('fuel', models.CharField(max_length=10)),
                ('max_load', models.IntegerField()),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.TextField(max_length=25)),
                ('destination', models.TextField(max_length=25)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('arrival_date', models.DateField()),
                ('max_price', models.FloatField()),
                ('freight_type', models.CharField(max_length=15)),
                ('weight', models.IntegerField()),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=50)),
                ('other_details', models.CharField(max_length=200)),
                ('clientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('freight_type', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('price_per_km', models.FloatField()),
                ('senderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('truckID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.truck')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.TextField(max_length=25)),
                ('destination', models.TextField(max_length=25)),
                ('date', models.DateField(auto_now_add=True)),
                ('freight_type', models.TextField(max_length=15)),
                ('final_price', models.FloatField()),
                ('km', models.FloatField()),
                ('senderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='auth.user')),
                ('transporterID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transporter', to='auth.user')),
                ('truckID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.truck')),
            ],
        ),
    ]
