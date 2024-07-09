# Generated by Django 5.0.6 on 2024-06-20 04:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venadApp', '0017_remove_purchasedetails_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedetails',
            name='vendor',
        ),
        migrations.AddField(
            model_name='purchased_products',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='venadApp.vendordetails'),
        ),
    ]