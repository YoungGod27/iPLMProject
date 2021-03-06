# Generated by Django 3.2.4 on 2021-07-05 07:15

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0039_auto_20210705_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdapplicant',
            name='hd_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 7, 15, 26, 438076, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loaapplicant',
            name='LOA_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 7, 15, 26, 438076, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ojtapplicant',
            name='ojt_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 7, 15, 26, 438076, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shifterapplicant',
            name='shifter_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 7, 15, 26, 438076, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spapplicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 5, 7, 15, 26, 438076, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transfereeapplicant',
            name='transfer_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 7, 15, 26, 438076, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='Email must be: @plm.edu.ph', regex='^[A-Za-z0-9._%+-]+@plm.edu.ph$')], verbose_name='email address'),
        ),
    ]
