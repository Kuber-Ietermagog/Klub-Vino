# Generated by Django 2.0.2 on 2018-07-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winetasting', '0012_auto_20180703_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='winetasting',
            name='created_by',
            field=models.CharField(default='', max_length=256),
        ),
    ]
