# Generated by Django 2.0.2 on 2018-06-29 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winetasting', '0003_auto_20180628_0918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='winetastinginfo',
            options={'ordering': ('wine_code_name',)},
        ),
        migrations.AlterField(
            model_name='winetastinginfo',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='winetastinginfo',
            name='points',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
    ]
