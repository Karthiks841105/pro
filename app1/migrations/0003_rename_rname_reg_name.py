# Generated by Django 3.2 on 2021-10-11 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_name_reg_rname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reg',
            old_name='rname',
            new_name='name',
        ),
    ]