# Generated by Django 4.1 on 2022-10-25 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_alter_itemtable_inventry_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtable',
            name='tax_rate',
        ),
    ]
