# Generated by Django 3.1.5 on 2021-02-04 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tom_dataproducts', '0008_auto_20191205_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reduceddatum',
            name='value',
            field=models.JSONField(),
        ),
    ]
