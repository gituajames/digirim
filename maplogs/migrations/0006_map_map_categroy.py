# Generated by Django 3.1.3 on 2021-08-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maplogs', '0005_auto_20210719_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='map_categroy',
            field=models.CharField(choices=[('Cadastral', 'cadastral maps'), ('General Boundary', 'general boundary')], default='Cadastral', max_length=100),
        ),
    ]
