# Generated by Django 3.1.3 on 2021-06-02 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maplogs', '0002_auto_20210517_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='stamped_county_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 2, 0, 42, 12, 939643)),
            preserve_default=False,
        ),
    ]
