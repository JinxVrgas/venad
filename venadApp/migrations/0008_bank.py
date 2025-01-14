# Generated by Django 5.0.6 on 2024-06-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venadApp', '0007_licenses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50, null=True)),
                ('bank_branch', models.CharField(max_length=50, null=True)),
                ('bank_address', models.CharField(max_length=50, null=True)),
                ('bank_account_no', models.CharField(max_length=50, null=True)),
                ('bank_ifsccode', models.CharField(max_length=50, null=True)),
                ('bank_balance', models.CharField(max_length=50, null=True)),
                ('bank_date', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
