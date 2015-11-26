# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('branch_name', models.CharField(default='', max_length=50)),
                ('branch_address', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('insurance_name', models.CharField(default='', max_length=50)),
                ('insurance_price', models.DecimalField(default='', decimal_places=2, max_digits=10)),
                ('insurance_limit', models.PositiveIntegerField(default='')),
                ('insurance_date_created', models.DateField(default=datetime.date.today)),
                ('insurance_validity_start', models.DateField(default=datetime.date.today)),
                ('insurance_validity_end', models.DateField(default=datetime.date.today)),
                ('insurance_age_start', models.PositiveIntegerField(default='')),
                ('insurance_age_end', models.PositiveIntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('position_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Underwriter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('underwriter_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('user_firstname', models.CharField(default='', max_length=50)),
                ('user_middlename', models.CharField(default='', max_length=50, blank=True)),
                ('user_lastname', models.CharField(default='', max_length=50)),
                ('position_name', models.ForeignKey(to='micro_insurance.Position')),
            ],
        ),
        migrations.AddField(
            model_name='insurance',
            name='insurance_underwriter',
            field=models.ForeignKey(to='micro_insurance.Underwriter'),
        ),
    ]
