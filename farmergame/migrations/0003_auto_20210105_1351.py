# Generated by Django 3.1.5 on 2021-01-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmergame', '0002_auto_20210105_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farm',
            old_name='starting_capital',
            new_name='capital',
        ),
        migrations.AlterField(
            model_name='ownanimal',
            name='nr_owned',
            field=models.IntegerField(default=0),
        ),
    ]