# Generated by Django 5.0.6 on 2024-06-18 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venadApp', '0016_rename_x_purchasedetails_vendor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedetails',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='cgst_amount',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='igst',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='igst_amount',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='net_amount',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='prate',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='product',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='sgst',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='sgst_amount',
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='taxable_amount',
        ),
        migrations.CreateModel(
            name='purchased_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.CharField(max_length=50, null=True)),
                ('unit', models.CharField(max_length=50, null=True)),
                ('prate', models.BigIntegerField(max_length=50, null=True)),
                ('MRP', models.BigIntegerField(max_length=50, null=True)),
                ('discount', models.BigIntegerField(max_length=50, null=True)),
                ('amount', models.BigIntegerField(max_length=50, null=True)),
                ('taxable_amount', models.BigIntegerField(max_length=50, null=True)),
                ('cgst', models.BigIntegerField(max_length=50, null=True)),
                ('cgst_amount', models.BigIntegerField(max_length=50, null=True)),
                ('sgst', models.BigIntegerField(max_length=50, null=True)),
                ('sgst_amount', models.BigIntegerField(max_length=50, null=True)),
                ('igst', models.BigIntegerField(max_length=50, null=True)),
                ('igst_amount', models.BigIntegerField(max_length=50, null=True)),
                ('net_amount', models.BigIntegerField(max_length=50, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='venadApp.products')),
                ('purchased_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='venadApp.purchasedetails')),
            ],
        ),
    ]
