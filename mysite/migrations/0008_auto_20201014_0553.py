# Generated by Django 3.1.2 on 2020-10-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20201014_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kiambuconstituencies',
            name='pop_densty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='kiambuconstituencies',
            name='population',
            field=models.IntegerField(null=True),
        ),
    ]