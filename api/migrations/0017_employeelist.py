# Generated by Django 3.2.4 on 2021-06-17 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20210616_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(default=0, max_length=70)),
                ('employee', models.CharField(default=0, max_length=70)),
                ('department', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]