# Generated by Django 4.0.3 on 2022-04-15 06:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecapr', '0007_alter_bet_pot_win'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bet',
            name='event_finish',
            field=models.DateField(default=datetime.date(2022, 4, 15)),
        ),
    ]