# Generated by Django 4.0.3 on 2022-04-11 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecapr', '0006_bet_pot_win_alter_bet_event_finish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='pot_win',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]