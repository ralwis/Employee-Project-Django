# Generated by Django 4.2 on 2023-04-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectemployeetable',
            name='employee',
        ),
        migrations.AddField(
            model_name='projectemployeetable',
            name='employee',
            field=models.ManyToManyField(to='employeeApp.employeetable'),
        ),
    ]
