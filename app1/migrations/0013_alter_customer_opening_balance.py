# Generated by Django 4.0.6 on 2022-10-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_customer_opening_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='opening_balance',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
