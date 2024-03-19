# Generated by Django 4.1.6 on 2023-03-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tom_targets', '0019_auto_20210811_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetname',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='The time at which this target name was created.'),
        ),
        migrations.AlterField(
            model_name='targetname',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='The time at which this target name was changed in the TOM database.', verbose_name='Last Modified'),
        ),
    ]
