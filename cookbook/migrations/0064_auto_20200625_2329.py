# Generated by Django 3.0.7 on 2020-06-25 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0063_auto_20200625_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='file_path',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='file_uid',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
