# Generated by Django 4.1 on 2022-10-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('zone', models.CharField(max_length=20)),
                ('street_name', models.CharField(max_length=256)),
                ('building_number', models.IntegerField(blank=True, null=True)),
                ('flat_number', models.IntegerField(blank=True, null=True)),
                ('land_mark', models.CharField(blank=True, max_length=256, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
