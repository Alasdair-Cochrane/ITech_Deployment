# Generated by Django 5.0.2 on 2024-03-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyStay', '0013_roomtype_guest_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomtype',
            old_name='guest_number',
            new_name='guests',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='country',
            field=models.CharField(blank=True, default='Great Britain', max_length=50),
        ),
    ]
