# Generated by Django 4.0.3 on 2022-04-09 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmaker', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('odds', models.IntegerField()),
                ('bet_type', models.CharField(max_length=50)),
                ('bet_market', models.CharField(max_length=75)),
                ('wager', models.IntegerField()),
                ('sport', models.CharField(max_length=50)),
                ('league', models.CharField(max_length=50)),
                ('notes', models.TextField()),
                ('date_placed', models.DateTimeField(auto_now_add=True)),
                ('date_resolved', models.DateTimeField(auto_now=True)),
                ('resolved', models.BooleanField()),
                ('bet_result', models.CharField(default='None', max_length=10)),
            ],
        ),
    ]
