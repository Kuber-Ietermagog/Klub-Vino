# Generated by Django 2.0.2 on 2018-06-29 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('winetasting', '0004_auto_20180629_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winetastinginfo',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proe_wyn', to='winetasting.WineTasting'),
        ),
    ]
