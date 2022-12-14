# Generated by Django 3.2.7 on 2021-12-31 19:19

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseRecord',
            fields=[
                ('record_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BaseRotation',
            fields=[
                ('rotation_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('school_name', models.CharField(choices=[('STI', 'Select Therapy Institute'), ('ST2', 'Select Therapy Institute Location 2'), ('ST3', 'Select Therapy Institute Location 3')], max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('instructor_email', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='BaseStudent',
            fields=[
                ('student_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('makeup_student', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CNARotation',
            fields=[
                ('baserotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gms.baserotation')),
                ('rotation_num', models.PositiveIntegerField()),
                ('instructor_title', models.CharField(choices=[('RN', 'Register Nurse'), ('LVN', 'Licensed Vocational Nurse')], max_length=50)),
                ('clinical_site', models.CharField(choices=[('Rowland', 'Rowland Convalescent Hospital'), ('Pinegrove', 'Pinegrove Healthcare and Wellness Centre'), ('Sunnyview', 'Sunnyview Care Center')], max_length=50)),
            ],
            options={
                'verbose_name': 'CNA Rotation',
            },
            bases=('gms.baserotation',),
        ),
        migrations.CreateModel(
            name='CNAStudent',
            fields=[
                ('basestudent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gms.basestudent')),
                ('rotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cna_students', related_query_name='cna_student', to='gms.cnarotation')),
            ],
            options={
                'verbose_name': 'CNA Student',
            },
            bases=('gms.basestudent',),
        ),
        migrations.CreateModel(
            name='HHARotation',
            fields=[
                ('baserotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gms.baserotation')),
                ('rotation_num', models.PositiveIntegerField()),
                ('instructor_title', models.CharField(choices=[('RN', 'Register Nurse'), ('LVN', 'Licensed Vocational Nurse')], max_length=50)),
                ('clinical_site', models.CharField(choices=[('Rowland', 'Rowland Convalescent Hospital'), ('Pinegrove', 'Pinegrove Healthcare and Wellness Centre'), ('Sunnyview', 'Sunnyview Care Center')], max_length=50)),
            ],
            options={
                'verbose_name': 'HHA Rotation',
            },
            bases=('gms.baserotation',),
        ),
        migrations.CreateModel(
            name='HHAStudent',
            fields=[
                ('basestudent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gms.basestudent')),
                ('rotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hha_students', related_query_name='hha_student', to='gms.hharotation')),
            ],
            options={
                'verbose_name': 'HHA Student',
            },
            bases=('gms.basestudent',),
        ),
        migrations.CreateModel(
            name='HHATheoryRecord',
            fields=[
                ('baserecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gms.baserecord')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('hours_spent', models.PositiveIntegerField()),
                ('test_score', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('topic', models.CharField(choices=[('Introduction to Aide and Agency Role', 'Introduction to Aide and Agency Role'), ('Interpretation of Medical and Social Needs of People Being Served', 'Interpretation of Medical and Social Needs of People Being Served'), ('Personal Care Services', 'Personal Care Services'), ('Nutrition', 'Nutrition'), ('Cleaning and Care Tasks in the Home', 'Cleaning and Care Tasks in the Home')], max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hha_theory_records', related_query_name='hha_theory_record', to='gms.hhastudent')),
            ],
            options={
                'verbose_name': 'HHA Theory Record',
            },
            bases=('gms.baserecord',),
        ),
        migrations.CreateModel(
            name='HHAClinicalRecord',
            fields=[
                ('baserecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gms.baserecord')),
                ('hours_spent', models.PositiveIntegerField()),
                ('comments', models.CharField(blank=True, max_length=200)),
                ('performance_satisfied', models.BooleanField(default=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('topic', models.CharField(choices=[('Personal Care Service', 'Personal Care Service'), ('Nutrition', 'Nutrition'), ('Cleaning and Care Tasks in the Home', 'Cleaning and Care Tasks in the Home')], max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hha_clinical_records', related_query_name='hha_clinical_record', to='gms.hhastudent')),
            ],
            options={
                'verbose_name': 'HHA Clinical Record',
            },
            bases=('gms.baserecord',),
        ),
        migrations.CreateModel(
            name='CNATheoryRecord',
            fields=[
                ('baserecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gms.baserecord')),
                ('hours_spent', models.PositiveIntegerField()),
                ('test_score', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('topic', models.CharField(choices=[('Module 1', (('Roles and responsibilities of a Certified Nurse Assistant (CNA)', 'Roles and responsibilities of a Certified Nurse Assistant (CNA)'), ('Title 22, Division 5, California Code of Regulations, overview', 'Title 22, Division 5, California Code of Regulations, overview'), ('Requirements for nurse assistant certification', 'Requirements for nurse assistant certification'), ('Professionalism', 'Professionalism'), ('Ethics and confidentiality', 'Ethics and confidentiality'), ('Module 1 Quiz', 'Module 1 Quiz'))), ('Module 2', (('Title 22 Section 72527', 'Title 22 Section 72527'), ('Health and Safety Code Sections 1599.1, 1599.2, 1599.3', 'Health and Safety Code Sections 1599.1, 1599.2, 1599.3'), ('Code of Federal Regulations Part 483 Sections 483.10, 483.12, 483.13, and 483.15', 'Code of Federal Regulations Part 483 Sections 483.10, 483.12, 483.13, and 483.15'), ('Preventing, recognizing, and reporting residents right violations', 'Preventing, recognizing, and reporting residents right violations'), ('Module 2 Quiz', 'Module 2 Quiz'))), ('Module 3', (('Communications', 'Communications'), ('Defense mechanisms', 'Defense mechanisms'), ('Sociocultural factors', 'Sociocultural factors'), ('Attitudes toward illness and health care', 'Attitudes toward illness and health care'), ('Family interaction', 'Family interaction'), ('Module 3 Quiz', 'Module 3 Quiz'))), ('Module 4', (('Emergency', 'Emergency'), ('General safety rules', 'General safety rules'), ('Fire and disaster plans', 'Fire and disaster plans'), ('Roles and procedures for CNA', 'Roles and procedures for CNA'), ('Patient safety', 'Patient safety'), ('Module 4 Quiz', 'Module 4 Quiz'))), ('Module 5', (('Basic body mechanics', 'Basic body mechanics'), ('Transfer techniques', 'Transfer techniques'), ('Ambulation', 'Ambulation'), ('Proper body mechanics / positioning techniques', 'Proper body mechanics / positioning techniques'), ('Module 5 Quiz', 'Module 5 Quiz'))), ('Module 6', (('Microorganisms', 'Microorganisms'), ('Universal precautions', 'Universal precautions'), ('Principles of asepsis', 'Principles of asepsis'), ('Module 6 Quiz', 'Module 6 Quiz'))), ('Module 7', (('Metric system', 'Metric system'), ('Weight, length, and liquid volume', 'Weight, length, and liquid volume'), ('Military time, i.e., a 24-hour clock', 'Military time, i.e., a 24-hour clock'), ('Module 7 Quiz', 'Module 7 Quiz'))), ('Module 8', (('Bathing / medicinal baths', 'Bathing / medicinal baths'), ('Dressing', 'Dressing'), ('Oral hygiene', 'Oral hygiene'), ('Hair care, shampoo, medicinal shampoo, nail care, shaving', 'Hair care, shampoo, medicinal shampoo, nail care, shaving'), ('Prosthetic devices', 'Prosthetic devices'), ('Skin care / decubitus ulcers', 'Skin care / decubitus ulcers'), ('Elimination needs', 'Elimination needs'), ('Bowel and bladder retraining', 'Bowel and bladder retraining'), ('Weigh and measure patient', 'Weigh and measure patient'), ('Module 8 Quiz', 'Module 8 Quiz'))), ('Module 9', (('Collection of specimens, including: stool, urine, and sputum', 'Collection of specimens, including: stool, urine, and sputum'), ('Care of patient with tubing, gastric, oxygen, urinary, IV', 'Care of patient with tubing, gastric, oxygen, urinary, IV'), ('Intake and Output', 'Intake and Output'), ('Bed making', 'Bed making'), ('Cleansing enemas, laxative suppositories', 'Cleansing enemas, laxative suppositories'), ('Admission, transfer, discharge', 'Admission, transfer, discharge'), ('Bandages, nonsterile dry dressing application of nonlegend topical ointments to intact skin', 'Bandages, nonsterile dry dressing application of nonlegend topical ointments to intact skin'), ('Module 9 Quiz', 'Module 9 Quiz'))), ('Module 10', (('Purpose of vital signs', 'Purpose of vital signs'), ('Factors affecting vital signs', 'Factors affecting vital signs'), ('Normal ranges', 'Normal ranges'), ('Methods of measurement', 'Methods of measurement'), ('Temperature, pulse, respiration', 'Temperature, pulse, respiration'), ('Blood pressure', 'Blood pressure'), ('Abnormalities', 'Abnormalities'), ('Recording', 'Recording'), ('Module 10 Quiz', 'Module 10 Quiz'))), ('Module 11', (('Proper nutrition', 'Proper nutrition'), ('Feeding technique', 'Feeding technique'), ('Diet therapy', 'Diet therapy'), ('Module 11 Quiz', 'Module 11 Quiz'))), ('Module 12', (('Signs and symptoms of distress', 'Signs and symptoms of distress'), ('Immediate and temporary intervention', 'Immediate and temporary intervention'), ('Emergency codes', 'Emergency codes'), ('Module 12 Quiz', 'Module 12 Quiz'))), ('Module 13', (('Special needs of persons with developmental and mental disorders', 'Special needs of persons with developmental and mental disorders'), ('Introduction to anatomy and physiology', 'Introduction to anatomy and physiology'), ('Physical and behavioral needs and changes', 'Physical and behavioral needs and changes'), ('Community resources available', 'Community resources available'), ('Psychological, social, and recreational needs', 'Psychological, social, and recreational needs'), ('Common diseases / disorders including signs and symptoms', 'Common diseases / disorders including signs and symptoms'), ('Module 13 Quiz', 'Module 13 Quiz'))), ('Module 14', ((')Promoting patient potential', 'Promoting patient potential'), ('Devices and equipment', 'Devices and equipment'), ('ADLs', 'ADLs'), ('Family interactions', 'Family interactions'), ('Complications of inactivity', 'Complications of inactivity'), ('Ambulation', 'Ambulation'), ('ROM', 'ROM'), ('Module 14 Quiz', 'Module 14 Quiz'))), ('Module 15', (('Observation of patients and reporting responsibilities', 'Observation of patients and reporting responsibilities'), ('Patient care plan', 'Patient care plan'), ('Patient care documentation', 'Patient care documentation'), ('Legal issues of charting', 'Legal issues of charting'), ('Medical terminology and abbreviations', 'Medical terminology and abbreviations'), ('Module 15 Quiz', 'Module 15 Quiz'))), ('Module 16', (('Stages of grief', 'Stages of grief'), ('Emotional and spiritual needs of patient and family', 'Emotional and spiritual needs of patient and family'), ('Rights of dying patient', 'Rights of dying patient'), ('Signs of approaching death', 'Signs of approaching death'), ('Monitoring the patient', 'Monitoring the patient'), ('Postmortem care', 'Postmortem care'), ('Module 16 Quiz', 'Module 16 Quiz'))), ('Module 17', (('Preventing, recognizing and reporting instances of resident abuse', 'Preventing, recognizing and reporting instances of resident abuse'), ('Module 17 Quiz', 'Module 17 Quiz')))], max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cna_theory_records', related_query_name='cna_theory_record', to='gms.cnastudent')),
            ],
            options={
                'verbose_name': 'CNA Theory Record',
            },
            bases=('gms.baserecord',),
        ),
        migrations.CreateModel(
            name='CNAClinicalRecord',
            fields=[
                ('baserecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gms.baserecord')),
                ('comments', models.CharField(blank=True, max_length=200)),
                ('performance_satisfied', models.BooleanField(default=True)),
                ('topic', models.CharField(choices=[('Module 2', (('Knocks on door before entering', 'Knocks on door before entering'), ('Pulls privacy curtains during personal care', 'Pulls privacy curtains during personal care'), ('Keeps resident information confidential', 'Keeps resident information confidential'), ('Treats resident with respect and dignity', 'Treats resident with respect and dignity'), ('Encourages resident to make choices', 'Encourages resident to make choices'), ('Explains procedure to resident', 'Explains procedure to resident'))), ('Module 4 and Module 12', (('Applying postural supports (safety devices)', 'Applying postural supports (safety devices)'), ('Applying soft wrist/ankle restraint as safety device', 'Applying soft wrist/ankle restraint as safety device'), ('Heimlich maneuver for the conscious resident', 'Heimlich maneuver for the conscious resident'), ('Heimlich maneuver for the unconscious resident', 'Heimlich maneuver for the unconscious resident'), ('Positioning of call light', 'Positioning of call light'), ('Demonstrates fire/disaster procedures', 'Demonstrates fire/disaster procedures'), ('Handles O2 safely', 'Handles O2 safely'), ('Use of fire extinguisher', 'Use of fire extinguisher'))), ('Module 5', (('Use of gait belt', 'Use of gait belt'), ('Helping the helpless resident up to the head of the bed with two assistants', 'Helping the helpless resident up to the head of the bed with two assistants'), ('Turning and positioning the resident - Supine', 'Turning and positioning the resident - Supine'), ('Turning and positioning the resident - Side-lying', 'Turning and positioning the resident - Side-lying'), ('Turning and positioning the resident - Use of lift sheet', 'Turning and positioning the resident - Use of lift sheet'), ('Assisting transfer from bed to chair or wheelchair', 'Assisting transfer from bed to chair or wheelchair'), ('Assisting transfer from chair or wheelchair to bed', 'Assisting transfer from chair or wheelchair to bed'), ('Mechanical lift', 'Mechanical lift'))), ('Module 6', (('Handwashing', 'Handwashing'), ('Proper handling of linen', 'Proper handling of linen'), ('Universal precautions - Gloving', 'Universal precautions - Gloving'), ('Universal precautions - Gowning', 'Universal precautions - Gowning'), ('Universal precautions - Apply mask', 'Universal precautions - Apply mask'), ('Double bagging trash/waste', 'Double bagging trash/waste'))), ('Module 7', (('Measuring oral intake', 'Measuring oral intake'), ('Measuring urinary output', 'Measuring urinary output'), ('Documents in military time', 'Documents in military time'))), ('Module 8', (('Back rub', 'Back rub'), ('Bed bath/partial bath', 'Bed bath/partial bath'), ('Tub bath', 'Tub bath'), ('Shower', 'Shower'), ('Assisting with oral hygiene', 'Assisting with oral hygiene'), ('Mouth care of the unconscious resident', 'Mouth care of the unconscious resident'), ('Denture care', 'Denture care'), ('Nail care', 'Nail care'), ("Combing the resident's hair", "Combing the resident's hair"), ('Shampoo of bedridden resident', 'Shampoo of bedridden resident'), ('Shampoo with shower or tub bath', 'Shampoo with shower or tub bath'), ('Medicinal shampoo', 'Medicinal shampoo'), ('Shaving - electrical shaver', 'Shaving - electrical shaver'), ('Shaving - razor blade', 'Shaving - razor blade'), ('Dressing and undressing the resident', 'Dressing and undressing the resident'), ('Changing the clothes of resident with IV', 'Changing the clothes of resident with IV'), ('Assist in the use of urinal', 'Assist in the use of urinal'), ('Assist in the use of the bedpan', 'Assist in the use of the bedpan'), ('Assisting resident to commode/toilet', 'Assisting resident to commode/toilet'), ('Bladder retraining', 'Bladder retraining'), ('Bowel retraining', 'Bowel retraining'), ('Perineal care', 'Perineal care'), ('Care and use of artificial limbs', 'Care and use of artificial limbs'), ('Use and application of splints', 'Use and application of splints'), ('Applying a behind-the-ear hearing aid', 'Applying a behind-the-ear hearing aid'), ('Removing a behind-the-ear hearing aid', 'Removing a behind-the-ear hearing aid'), ('Measuring the height of resident in bed', 'Measuring the height of resident in bed'), ('Weighing the resident in bed', 'Weighing the resident in bed'), ('Measuring and weighing the resident using an upright scale', 'Measuring and weighing the resident using an upright scale'))), ('Module 9', (('Collect and identify specimen - Sputum specimen', 'Collect and identify specimen - Sputum specimen'), ('Collect and identify specimen - Urine specimen: clean catch', 'Collect and identify specimen - Urine specimen: clean catch'), ('Collect and identify specimen - Stool specimen', 'Collect and identify specimen - Stool specimen'), ('Occupied bed making', 'Occupied bed making'), ('Unoccupied bed making', 'Unoccupied bed making'), ('Administering the commercially prepared cleansing enema', 'Administering the commercially prepared cleansing enema'), ('Administering enemas - tap water, soap suds', 'Administering enemas - tap water, soap suds'), ('Administering laxative suppository', 'Administering laxative suppository'), ('Empty urinary bags', 'Empty urinary bags'), ('Care of resident with tubing - Oxygen', 'Care of resident with tubing - Oxygen'), ('Care of resident with tubing - IV', 'Care of resident with tubing - IV'), ('Care of resident with tubing - Gastrostomy', 'Care of resident with tubing - Gastrostomy'), ('Care of resident with tubing - Nasogastric', 'Care of resident with tubing - Nasogastric'), ('Care of resident with tubing - Urinary catheter', 'Care of resident with tubing - Urinary catheter'), ('Antiembolic hose, elastic stockings (TED Hose)', 'Antiembolic hose, elastic stockings (TED Hose)'), ('Admitting the resident', 'Admitting the resident'), ('Transferring the resident', 'Transferring the resident'), ('Discharging the resident', 'Discharging the resident'), ('Application of nonsterile dressing', 'Application of nonsterile dressing'), ('Application of nonlegend topical ointments', 'Application of nonlegend topical ointments'))), ('Module 10', (('Temperature - Oral', 'Temperature - Oral'), ('Temperature - Axillary', 'Temperature - Axillary'), ('Temperature - Rectal', 'Temperature - Rectal'), ('Temperature - Electronic', 'Temperature - Electronic'), ('Pulse - radial', 'Pulse - radial'), ('Pulse - apical', 'Pulse - apical'), ('Respiration', 'Respiration'), ('Blood pressure', 'Blood pressure'))), ('Module 11', (('Feeding the helpless resident', 'Feeding the helpless resident'), ('Assisting the resident who can feed self', 'Assisting the resident who can feed self'), ('Verifying that resident has been given correct diet tray', 'Verifying that resident has been given correct diet tray'), ('Use of feeding assistance devices', 'Use of feeding assistance devices'))), ('Module 13', (('Use of dementia-related communication skills', 'Use of dementia-related communication skills'), ('Identify your name and purpose of interaction', 'Identify your name and purpose of interaction'), ("Make eye contact at patient's eye level", "Make eye contact at patient's eye level"), ('Use of continuum of verbal and other non-physical techniques', 'Use of continuum of verbal and other non-physical techniques'))), ('Module 14', (('Range of motion exercises', 'Range of motion exercises'), ('Assisting the resident to ambulate with gait belt', 'Assisting the resident to ambulate with gait belt'), ('Assisting the resident to ambulate with walker', 'Assisting the resident to ambulate with walker'), ('Assisting the resident to ambulate with cane', 'Assisting the resident to ambulate with cane'), ('Rehabilitative devices', 'Rehabilitative devices'))), ('Module 15', (('Reports appropriate information to change nurse', 'Reports appropriate information to change nurse'), ('Documents V/S, ADLs timely/correctly', 'Documents V/S, ADLs timely/correctly'), ("Documents changes in resident's body functions/behavior", "Documents changes in resident's body functions/behavior"), ('Participates in resident care planning', 'Participates in resident care planning')))], max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cna_clinical_records', related_query_name='cna_clinical_record', to='gms.cnastudent')),
            ],
            options={
                'verbose_name': 'CNA Clinical Record',
            },
            bases=('gms.baserecord',),
        ),
    ]
