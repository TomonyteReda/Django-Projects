# Generated by Django 3.2.13 on 2022-05-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0002_auto_20220523_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(null=True, upload_to='car_photos', verbose_name='Car Photo'),
        ),
    ]