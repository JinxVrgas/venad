# Generated by Django 5.0.6 on 2024-06-11 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venadApp', '0010_productcategory_taxmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.IntegerField()),
                ('supplier_name', models.CharField(max_length=100, null=True)),
                ('purchase_date', models.CharField(max_length=10, null=True)),
                ('item_count', models.IntegerField()),
                ('totalprice', models.BigIntegerField()),
            ],
        ),
    ]
