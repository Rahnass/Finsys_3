# Generated by Django 4.0.6 on 2022-10-06 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorder',
            name='description',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='description1',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='description3',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='hsn',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='hsn1',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='hsn2',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='hsn3',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='product',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='product1',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='product2',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='product3',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='qty1',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='qty2',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='qty3',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='rate1',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='rate2',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='rate3',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='tax1',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='tax2',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='tax3',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='taxamount',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='total',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='total1',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='total2',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='total3',
        ),
        migrations.CreateModel(
            name='sales_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('hsn', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('qty', models.IntegerField(default=0, null=True)),
                ('price', models.CharField(max_length=100)),
                ('total', models.IntegerField(default=0, null=True)),
                ('tax', models.CharField(max_length=100)),
                ('salesorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.salesorder')),
            ],
        ),
    ]