# Generated by Django 3.0.7 on 2020-09-21 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0079_invitelink_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreference',
            name='shopping_auto_sync',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='invitelink',
            name='valid_until',
            field=models.DateField(default=datetime.date(2020, 10, 5)),
        ),
    ]
