# Generated by Django 3.2 on 2021-10-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pas', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('loc', models.CharField(max_length=50)),
            ],
        ),
    ]