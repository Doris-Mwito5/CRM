# Generated by Django 5.0.4 on 2024-04-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(),
        ),
    ]
