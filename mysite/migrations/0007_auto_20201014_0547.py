# Generated by Django 3.1.2 on 2020-10-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20201014_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kiambucounty',
            name='remarks_2',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
