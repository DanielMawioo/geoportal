# Generated by Django 3.1.2 on 2020-10-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20201014_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kiambucounty',
            name='cc_2',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='kiambucounty',
            name='engtype_2',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='kiambucounty',
            name='hasc_2',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='kiambucounty',
            name='nl_name_2',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='kiambucounty',
            name='type_2',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
