# Generated by Django 3.2.7 on 2022-03-30 04:05

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0007_alter_student_starting_wage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='starting_wage',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='USD', max_digits=10),
        ),
    ]
