# Generated by Django 4.2.7 on 2023-12-07 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('capital_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('capital_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.capital', unique=True)),
            ],
        ),
    ]
