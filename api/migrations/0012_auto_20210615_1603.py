# Generated by Django 3.1 on 2021-06-15 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210614_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='joining',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salary',
            name='leaving',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
