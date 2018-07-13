# Generated by Django 2.0.2 on 2018-06-27 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WineTasting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cultivar', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('hosted_by', models.CharField(max_length=250)),
                ('qty_wines', models.IntegerField()),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='WineTastingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('wine_code_name', models.CharField(max_length=10)),
                ('points', models.DecimalField(decimal_places=2, max_digits=4)),
                ('comments', models.TextField()),
                ('cultivar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasting', to='winetasting.WineTasting')),
            ],
        ),
    ]
