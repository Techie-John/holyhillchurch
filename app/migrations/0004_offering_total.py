# Generated by Django 4.2.5 on 2024-03-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_attendance_total_alter_attendance_childrenfemale_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='total',
            field=models.CharField(default='0', max_length=100, verbose_name='Total numbers'),
        ),
    ]
