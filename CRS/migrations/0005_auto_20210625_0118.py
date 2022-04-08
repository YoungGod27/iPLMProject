# Generated by Django 3.2.4 on 2021-06-24 17:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0004_auto_20210624_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='collegeDesc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='College Description'),
        ),
        migrations.AddField(
            model_name='department',
            name='courseDesc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Course Description'),
        ),
        migrations.AlterField(
            model_name='hdapplicant',
            name='hd_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 17, 18, 41, 315716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loaapplicant',
            name='LOA_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 17, 18, 41, 315716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ojtapplicant',
            name='ojt_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 17, 18, 41, 315716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shifterapplicant',
            name='shifter_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 17, 18, 41, 315716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spapplicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 24, 17, 18, 41, 315716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transfereeapplicant',
            name='transfer_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 17, 18, 41, 315716, tzinfo=utc)),
        ),
    ]
