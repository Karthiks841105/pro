# Generated by Django 4.1.3 on 2023-01-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_pho4_alter_pho_id_alter_pho1_id_alter_pho2_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='loc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=100)),
                ('lang', models.CharField(max_length=100)),
            ],
        ),
    ]
