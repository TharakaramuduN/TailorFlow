# Generated by Django 4.2.6 on 2023-12-09 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TailorFlow', '0014_alter_customers_profilephoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 9, 7, 30, 29, 586763, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
