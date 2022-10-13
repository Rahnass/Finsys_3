# Generated by Django 4.1 on 2022-10-13 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_rename_reason_stockreason'),
    ]

    operations = [
        migrations.CreateModel(
            name='stockadjust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(default='', max_length=100)),
                ('ref_no', models.CharField(default='', max_length=100)),
                ('date', models.CharField(default='', max_length=100)),
                ('account', models.CharField(blank=True, max_length=100, null=True)),
                ('reason', models.CharField(default='', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('attach', models.FileField(default='', upload_to='')),
                ('item1', models.CharField(max_length=100, null=True)),
                ('qty1', models.CharField(max_length=100, null=True)),
                ('qty_hand1', models.CharField(default='', max_length=100)),
                ('new_qty1', models.CharField(default='', max_length=100)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
