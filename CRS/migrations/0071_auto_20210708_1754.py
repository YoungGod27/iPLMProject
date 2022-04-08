# Generated by Django 3.2.4 on 2021-07-08 09:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0070_auto_20210708_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocksection',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='CRS.college', verbose_name='College'),
        ),
        migrations.AlterField(
            model_name='crsgrade',
            name='studentID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRS.studentinfo', verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='department',
            name='chairperson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='CRS.chairpersoninfo'),
        ),
        migrations.AlterField(
            model_name='hdapplicant',
            name='hd_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 9, 54, 13, 327647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hdapplicant',
            name='studentID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRS.studentinfo', verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='hdclearanceform',
            name='studentID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRS.studentinfo', verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='loaapplicant',
            name='LOA_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 9, 54, 13, 327647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loaapplicant',
            name='studentID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRS.studentinfo', verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='ojtapplicant',
            name='ojt_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 9, 54, 13, 327647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ojtapplicant',
            name='studentID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRS.studentinfo', verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='shifterapplicant',
            name='shifter_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 9, 54, 13, 327647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spapplicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 9, 54, 13, 327647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spapplicant',
            name='studentID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRS.studentinfo', verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='transfereeapplicant',
            name='transfer_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 9, 54, 13, 327647, tzinfo=utc)),
        ),
    ]
