# Generated by Django 4.0.4 on 2022-06-22 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DH_service', '0002_remove_send_data_keyword_send_data_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='send_data',
            name='title',
        ),
    ]