# Generated by Django 2.2.18 on 2021-04-22 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210407_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 13, 12, 36, 899293, tzinfo=utc)),
        ),
    ]
