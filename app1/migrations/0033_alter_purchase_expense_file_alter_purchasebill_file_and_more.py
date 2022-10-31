# Generated by Django 4.0.4 on 2022-10-04 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_purchase_expense_alter_purchasebill_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_expense',
            name='file',
            field=models.FileField(null=True, upload_to='purchase/expense'),
        ),
        migrations.AlterField(
            model_name='purchasebill',
            name='file',
            field=models.FileField(null=True, upload_to='purchase/bill'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='file',
            field=models.FileField(null=True, upload_to='purchase/purchaseorder'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='companyname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='lastname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='pincode',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='title',
            field=models.CharField(max_length=10, null=True),
        ),
    ]