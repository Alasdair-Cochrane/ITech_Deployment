# Generated by Django 5.0.2 on 2024-02-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyStay', '0010_alter_booking_check_in_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]
