# Generated by Django 4.1 on 2022-10-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_alter_reservation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Acceptance'), ('3', 'Rejected')], default='1', max_length=15),
        ),
    ]
