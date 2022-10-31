# Generated by Django 4.0.4 on 2022-09-30 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_alter_mjournal_account1_alter_mjournal_account2'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchasebill',
            fields=[
                ('billid', models.AutoField(primary_key=True, serialize=False, verbose_name='bid')),
                ('vendor_name', models.CharField(max_length=100)),
                ('billing_address', models.TextField()),
                ('bill_no', models.IntegerField(default=1000)),
                ('sourceofsupply', models.CharField(max_length=100, null=True)),
                ('destiofsupply', models.CharField(max_length=100, null=True)),
                ('branch', models.CharField(max_length=100, null=True)),
                ('reference', models.CharField(max_length=100, null=True)),
                ('contact_name', models.CharField(max_length=255, null=True)),
                ('deliverto', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
                ('deliver_date', models.DateField(null=True)),
                ('credit_period', models.CharField(max_length=100, null=True)),
                ('due_date', models.CharField(max_length=100, null=True)),
                ('sub_total', models.CharField(max_length=100, null=True)),
                ('sgst', models.CharField(max_length=100, null=True)),
                ('cgst', models.CharField(max_length=100, null=True)),
                ('igst', models.CharField(max_length=100, null=True)),
                ('discount', models.CharField(default=0, max_length=100)),
                ('tcs', models.CharField(max_length=100, null=True)),
                ('tcs_amount', models.CharField(max_length=100, null=True)),
                ('round_off', models.CharField(max_length=100, null=True)),
                ('tax_amount', models.CharField(max_length=100, null=True)),
                ('grand_total', models.CharField(max_length=100, null=True)),
                ('note', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(default=None, upload_to='purchaseorder')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Billed', 'Billed')], default='Draft', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='purchaseorder',
            fields=[
                ('porderid', models.AutoField(primary_key=True, serialize=False, verbose_name='pid')),
                ('vendor_name', models.CharField(max_length=100)),
                ('billing_address', models.TextField()),
                ('puchaseorder_no', models.IntegerField(default=1000)),
                ('sourceofsupply', models.CharField(max_length=100, null=True)),
                ('destiofsupply', models.CharField(max_length=100, null=True)),
                ('branch', models.CharField(max_length=100, null=True)),
                ('reference', models.CharField(max_length=100, null=True)),
                ('contact_name', models.CharField(max_length=255, null=True)),
                ('deliverto', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
                ('deliver_date', models.DateField(null=True)),
                ('credit_period', models.CharField(max_length=100, null=True)),
                ('due_date', models.CharField(max_length=100, null=True)),
                ('sub_total', models.CharField(max_length=100, null=True)),
                ('sgst', models.CharField(max_length=100, null=True)),
                ('cgst', models.CharField(max_length=100, null=True)),
                ('igst', models.CharField(max_length=100, null=True)),
                ('discount', models.CharField(default=0, max_length=100)),
                ('tcs', models.CharField(max_length=100, null=True)),
                ('tcs_amount', models.CharField(max_length=100, null=True)),
                ('round_off', models.CharField(max_length=100, null=True)),
                ('tax_amount', models.CharField(max_length=100, null=True)),
                ('grand_total', models.CharField(max_length=100, null=True)),
                ('note', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(default=None, upload_to='purchaseorder')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Approved', 'Approved'), ('Billed', 'Billed')], default='Draft', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('vendorid', models.AutoField(primary_key=True, serialize=False, verbose_name='VENID')),
                ('title', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('companyname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('website', models.CharField(default='', max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('gsttype', models.CharField(max_length=100, null=True)),
                ('gstin', models.CharField(default='', max_length=100)),
                ('panno', models.CharField(max_length=100, null=True)),
                ('sourceofsupply', models.CharField(max_length=100, null=True)),
                ('currency', models.CharField(max_length=100, null=True)),
                ('openingbalance', models.CharField(max_length=100, null=True)),
                ('paymentterms', models.CharField(max_length=100, null=True)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('shipstreet', models.CharField(max_length=100, null=True)),
                ('shipcity', models.CharField(max_length=100, null=True)),
                ('shipstate', models.CharField(max_length=100, null=True)),
                ('shippincode', models.CharField(max_length=100, null=True)),
                ('shipcountry', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='porder_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('amount', models.CharField(max_length=100, null=True)),
                ('pid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='bill_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('amount', models.CharField(max_length=100, null=True)),
                ('bid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasebill')),
            ],
        ),
    ]