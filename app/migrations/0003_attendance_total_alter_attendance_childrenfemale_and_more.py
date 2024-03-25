# Generated by Django 4.2.5 on 2024-03-25 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_offering'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='total',
            field=models.CharField(default='0', max_length=100, verbose_name='Total numbers'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='childrenFemale',
            field=models.CharField(max_length=100, verbose_name='Number of children females'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='childrenMale',
            field=models.CharField(max_length=100, verbose_name='Number of children males'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='female',
            field=models.CharField(max_length=100, verbose_name='Number of females'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='male',
            field=models.CharField(max_length=100, verbose_name='Number of males'),
        ),
    ]