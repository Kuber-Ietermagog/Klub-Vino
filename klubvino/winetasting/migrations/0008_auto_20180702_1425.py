# Generated by Django 2.0.2 on 2018-07-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winetasting', '0007_winetastingresults_user_searched'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='winetastingresults',
            options={'ordering': ('-total',)},
        ),
        migrations.AddField(
            model_name='winetasting',
            name='close_tasting',
            field=models.BooleanField(default=False),
        ),
    ]
