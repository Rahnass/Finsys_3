# Generated by Django 4.0.6 on 2022-10-11 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_payment_referno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='findinvoice',
        ),
    ]
