# Generated by Django 4.2.7 on 2023-11-30 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_cones', '0006_account_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='timeDelivered',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='timeOrdered',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='timeToDeliver',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
