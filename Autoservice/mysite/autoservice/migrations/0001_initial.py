# Generated by Django 3.2.13 on 2022-05-17 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_registration_no', models.CharField(max_length=100, verbose_name='Country registration number')),
                ('vin_code', models.CharField(max_length=100, verbose_name='VIN')),
                ('client', models.CharField(help_text='Client name and surname', max_length=100, verbose_name='Country registration number')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('car_model', models.CharField(max_length=100, verbose_name='Model')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(verbose_name='Order Date')),
                ('order_amount', models.FloatField(verbose_name='Order Amount')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.car')),
            ],
            options={
                'ordering': ['order_date'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100, verbose_name='Service name')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True, verbose_name='Quantity')),
                ('price', models.FloatField(verbose_name='Price')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.order')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.service')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.carmodel'),
        ),
    ]
