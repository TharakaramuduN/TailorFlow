# Generated by Django 4.2.6 on 2023-11-04 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TailorFlow', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='Photo',
        ),
    ]
