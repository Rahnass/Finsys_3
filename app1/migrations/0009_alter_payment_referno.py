# Generated by Django 4.0.6 on 2022-10-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_payment_paymdate_alter_paymentitems_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='referno',
            field=models.CharField(max_length=255),
        ),
    ]