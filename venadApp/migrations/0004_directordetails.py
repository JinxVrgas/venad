# Generated by Django 5.0.6 on 2024-06-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venadApp', '0003_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('father_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(null=True)),
                ('address', models.CharField(max_length=350)),
                ('e_mail', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('pan', models.CharField(max_length=255)),
                ('aadhar', models.CharField(max_length=255)),
                ('din', models.CharField(max_length=255)),
            ],
        ),
    ]
