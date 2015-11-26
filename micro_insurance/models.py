from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

class Insurance(models.Model):
    insurance_name = models.CharField(max_length=50, blank=False, default='')
    insurance_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default='')
    insurance_limit = models.PositiveIntegerField(blank=False, default='')
    insurance_date_created = models.DateField(default=date.today)
    insurance_validity_start = models.DateField(default=date.today)
    insurance_validity_end = models.DateField(default=date.today)
    insurance_age_start = models.PositiveIntegerField(default='')
    insurance_age_end = models.PositiveIntegerField(default='')
    insurance_underwriter = models.ForeignKey('Underwriter')

    def __str__(self):
        return(self.insurance_name)


class Underwriter(models.Model):
    underwriter_name = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        return(self.underwriter_name)


class Branch(models.Model):
    branch_name = models.CharField(max_length=50, blank=False, default='')
    branch_address = models.CharField(max_length=100, blank=False, default='')

    class Meta:
        verbose_name_plural = 'Branches'

class Position(models.Model):
    position_name = models.CharField(max_length=50, blank=False, default='')
    
class User(models.Model):
    username = models.CharField(max_length=50, blank=False, default='')
    password = models.CharField(max_length=50, blank=False, default='')
    user_firstname = models.CharField(max_length=50, blank=False, default='')
    user_middlename = models.CharField(max_length=50, blank=True, default='')
    user_lastname = models.CharField(max_length=50, blank=False, default='')
    position_name = models.ForeignKey(Position)



