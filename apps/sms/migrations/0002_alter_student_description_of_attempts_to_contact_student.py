from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='description_of_attempts_to_contact_student',
            field=models.TextField(blank=True, default='Information provided by ST office contacting students via phone/text/email.'),
        ),
    ]
