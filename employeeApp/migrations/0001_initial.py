# Generated by Django 4.2 on 2023-04-15 07:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employeeTable',
            fields=[
                ('Eid', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(default='', max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('designation', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='projectTable',
            fields=[
                ('Pid', models.AutoField(primary_key=True, serialize=False)),
                ('projectName', models.CharField(max_length=50)),
                ('startedDate', models.DateField(null=True)),
                ('description', models.TextField()),
                ('leader', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='employeeApp.employeetable')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectEmployeeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeApp.employeetable')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeApp.projecttable')),
            ],
        ),
    ]
