# Generated by Django 4.2.7 on 2023-12-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TailorFlow', '0009_alter_transactions_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='profilephoto',
            field=models.ImageField(default='images\\profilephotos\\Default_pfp.svg.png', upload_to='images/profilephotos'),
        ),
    ]
