# Generated by Django 4.0.4 on 2022-05-16 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=500)),
                ('age', models.PositiveIntegerField()),
                ('sex', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('others', 'OTHERS')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scheduler.staff')),
            ],
            bases=('scheduler.staff',),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scheduler.staff')),
                ('speciality', models.CharField(max_length=500)),
                ('qualification', models.CharField(max_length=500)),
            ],
            bases=('scheduler.staff',),
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scheduler.staff')),
            ],
            bases=('scheduler.staff',),
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scheduler.staff')),
            ],
            bases=('scheduler.staff',),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('symptoms', models.CharField(max_length=500)),
                ('diganosis', models.CharField(max_length=50)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scheduler.patient')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scheduler.doctor')),
            ],
        ),
    ]