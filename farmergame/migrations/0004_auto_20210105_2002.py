# Generated by Django 3.1.5 on 2021-01-05 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmergame', '0003_auto_20210105_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farm',
            old_name='farm_name',
            new_name='name',
        ),
    ]