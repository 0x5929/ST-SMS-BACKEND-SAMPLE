# Generated by Django 3.2.7 on 2022-03-15 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'User Accounts'},
        ),
    ]
