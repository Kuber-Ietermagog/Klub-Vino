# Generated by Django 2.0.2 on 2018-07-02 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('winetasting', '0008_auto_20180702_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineTastingFinal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_results', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='final_results', to='winetasting.WineTastingResults')),
            ],
        ),
    ]
