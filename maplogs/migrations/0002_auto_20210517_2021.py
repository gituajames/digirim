# Generated by Django 3.1.3 on 2021-05-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maplogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='scanned',
            field=models.BooleanField(default='True'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='upload_date',
            field=models.DateField(auto_now=True),
        ),
    ]
