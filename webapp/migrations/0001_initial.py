# Generated by Django 4.2.7 on 2023-12-10 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_history', models.CharField(max_length=50)),
                ('allergies', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.CharField(max_length=50)),
                ('dosage', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('medicalhistory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.medicalhistory')),
                ('patientinfo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.patientinfo')),
            ],
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='patientinfo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.patientinfo'),
        ),
        migrations.CreateModel(
            name='InsuranceInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=50)),
                ('patientinfo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.patientinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('reason', models.CharField(max_length=50)),
                ('patientinfo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.patientinfo')),
            ],
        ),
    ]
