# Generated by Django 2.0.2 on 2018-06-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_calendar', '0004_evententry_last_update_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evententry',
            name='last_update_by',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
