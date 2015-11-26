# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('insurance_name', models.CharField(default='Default', max_length=50)),
                ('insurance_price', models.DecimalField(decimal_places=2, default='0', max_digits=10)),
                ('insurance_limit', models.CharField(default='0', max_length=10)),
                ('insurance_date_created', models.DateField(default=datetime.date.today)),
                ('insurance_validity_start', models.DateField(default=datetime.date.today)),
                ('insurance_validity_end', models.DateField(default=datetime.date.today)),
                ('insurance_age_start', models.IntegerField(default='0')),
                ('insurance_age_end', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Underwriter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('underwriter_name', models.CharField(default='Default', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='insurance',
            name='insurance_underwriter',
            field=models.ForeignKey(to='micro_insurance.Underwriter'),
        ),
    ]
