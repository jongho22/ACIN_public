# Generated by Django 4.0.4 on 2022-06-23 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DH_service', '0008_alter_send_data_end_day_alter_send_data_start_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send_data',
            name='end_day',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='send_data',
            name='start_day',
            field=models.DateTimeField(),
        ),
    ]
