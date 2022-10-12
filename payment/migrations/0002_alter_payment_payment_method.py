# Generated by Django 4.1 on 2022-10-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('1', 'Cash'), ('2', 'Credit Or Debit Card'), ('3', 'Paypal')], default='1', max_length=25),
        ),
    ]