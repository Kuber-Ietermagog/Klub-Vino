# Generated by Django 2.0.2 on 2018-06-22 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_calendar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evententry',
            name='created_by',
        ),
    ]