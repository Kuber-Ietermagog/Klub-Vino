# Generated by Django 2.0.2 on 2018-06-29 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_calendar', '0005_auto_20180622_1309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evententry',
            options={'ordering': ('-date',)},
        ),
    ]