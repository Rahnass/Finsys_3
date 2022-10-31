# Generated by Django 4.0.6 on 2022-09-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_alter_salesorder_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Approved', 'Approved'), ('Sales Order', 'Sales Order')], default='Draft', max_length=150),
        ),
    ]