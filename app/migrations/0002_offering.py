# Generated by Django 4.2.5 on 2024-03-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('main_church_offering', models.CharField(max_length=100, verbose_name='Main Church Offering')),
                ('children_church_offering', models.CharField(max_length=100, verbose_name='Children Church Offering')),
                ('tithe', models.CharField(max_length=100, verbose_name='Tithes')),
            ],
        ),
    ]