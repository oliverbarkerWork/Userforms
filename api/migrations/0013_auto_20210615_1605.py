# Generated by Django 3.1 on 2021-06-15 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210615_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='joining',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='leaving',
        ),
    ]