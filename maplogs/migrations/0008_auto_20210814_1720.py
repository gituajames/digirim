# Generated by Django 3.1.3 on 2021-08-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maplogs', '0007_auto_20210814_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='county',
            field=models.CharField(choices=[('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Nyeri', 'Nyeri')], default='Laikipia', max_length=50),
        ),
    ]