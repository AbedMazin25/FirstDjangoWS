# Generated by Django 3.1.7 on 2021-03-03 17:11

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20210227_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='estimated_date',
        ),
        migrations.AddField(
            model_name='task',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 17, 11, 4, 224462, tzinfo=utc), verbose_name='date_added'),
        ),
        migrations.AddField(
            model_name='task',
            name='estimated_dur',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='task',
            name='infor',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
