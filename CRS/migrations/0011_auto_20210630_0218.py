# Generated by Django 3.2.4 on 2021-06-29 18:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0010_auto_20210630_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='currchecklist',
            name='semTaken',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('Summer', 'Summer')], max_length=50, null=True, verbose_name='School Sem'),
        ),
        migrations.AddField(
            model_name='currchecklist',
            name='yearTaken',
            field=models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year'), ('5', '5th Year'), ('6', '6th Year')], max_length=50, null=True, verbose_name='Year Taken'),
        ),
        migrations.AlterField(
            model_name='hdapplicant',
            name='hd_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 18, 18, 3, 833480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loaapplicant',
            name='LOA_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 18, 18, 3, 833480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ojtapplicant',
            name='ojt_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 18, 18, 3, 833480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shifterapplicant',
            name='shifter_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 18, 18, 3, 833480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spapplicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 29, 18, 18, 3, 833480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transfereeapplicant',
            name='transfer_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 18, 18, 3, 833480, tzinfo=utc)),
        ),
    ]