# Generated by Django 5.0.6 on 2024-06-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venadApp', '0023_damaged_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='damaged_products',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
