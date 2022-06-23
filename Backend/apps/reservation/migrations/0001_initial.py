# Generated by Django 3.2.12 on 2022-06-23 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('n_desktop', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'Desktop',
                'verbose_name_plural': 'Desktops',
                'ordering': ['n_desktop'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('n_hours', models.SmallIntegerField(default=8, verbose_name='Cantidad de horas a reservar')),
                ('desktop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.desktop')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
    ]
