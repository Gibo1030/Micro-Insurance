# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('branch_name', models.CharField(max_length=50, default='')),
                ('branch_address', models.CharField(max_length=100, default='')),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('insurance_name', models.CharField(max_length=30, default='', verbose_name='SKU Name')),
                ('insurance_base_price', models.DecimalField(decimal_places=2, max_digits=3, default='', verbose_name='SKU Base Price')),
                ('insurance_selling_price', models.DecimalField(decimal_places=2, max_digits=3, default='', verbose_name='SKU Selling Price')),
                ('insurance_limit', models.PositiveIntegerField(default='', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='SKU Limit')),
                ('insurance_date_created', models.DateField(editable=False, default=datetime.date.today, verbose_name='SKU Date Created')),
                ('insurance_days_covered', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(365)], verbose_name='SKU Days Covered')),
                ('insurance_age_start', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='SKU Age From')),
                ('insurance_age_end', models.PositiveIntegerField(default='', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='SKU Age To')),
            ],
            options={
                'verbose_name': 'SKU',
            },
        ),
        migrations.CreateModel(
            name='MicroInsuranceCompany',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('micro_insurance_name', models.CharField(max_length=50, default='', verbose_name='Micro Insurance Company Name')),
            ],
            options={
                'verbose_name_plural': 'Micro Insurance Company',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('position_name', models.CharField(max_length=50, default='', blank=True, verbose_name='User Role')),
            ],
            options={
                'verbose_name': 'User Role',
            },
        ),
        migrations.CreateModel(
            name='Underwriter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('underwriter_name', models.CharField(max_length=50, default='')),
                ('underwriter_contact_person', models.CharField(max_length=20, default='')),
                ('underwriter_contact_number', models.CharField(max_length=15, default='')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50, default='')),
                ('password', models.CharField(max_length=50, default='')),
                ('user_firstname', models.CharField(max_length=50, default='', verbose_name='First Name')),
                ('user_middlename', models.CharField(max_length=50, default='', blank=True, verbose_name='Middle Name(optional)')),
                ('user_lastname', models.CharField(max_length=50, default='', verbose_name='Last Name')),
                ('position_name', models.ForeignKey(to='micro_insurance.Position')),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
        migrations.AddField(
            model_name='insurance',
            name='insurance_underwriter',
            field=models.ForeignKey(to='micro_insurance.Underwriter'),
        ),
        migrations.AddField(
            model_name='branch',
            name='micro_insurance_name',
            field=models.ForeignKey(to='micro_insurance.MicroInsuranceCompany', verbose_name='Micro Insurance Company'),
        ),
        migrations.AddField(
            model_name='branch',
            name='username',
            field=models.ForeignKey(to='micro_insurance.UserProfile', verbose_name='Branch Manager'),
        ),
    ]
