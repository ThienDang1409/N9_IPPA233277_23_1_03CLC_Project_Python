# Generated by Django 4.2.6 on 2023-11-23 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gameplayer_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('bdate', models.DateField()),
                ('gmail', models.TextField()),
                ('level', models.TextField()),
                ('name', models.TextField()),
                ('sex', models.TextField()),
                ('time_now', models.IntegerField()),
                ('time_play', models.IntegerField()),
            ],
        ),
    ]