# Generated by Django 2.1.3 on 2018-11-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20181124_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='recover',
            field=models.BooleanField(default=False),
        ),
    ]
