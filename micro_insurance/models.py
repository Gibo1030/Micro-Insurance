from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator

class Underwriter(models.Model):
    underwriter_name = models.CharField(max_length=50, blank=False, default='')
    underwriter_contact_person = models.CharField(max_length=20, blank=False, default='')
    underwriter_contact_number = models.CharField(max_length=15, blank=False, default='')

    def __str__(self):
        return(self.underwriter_name)

class Insurance(models.Model):
    insurance_name = models.CharField(max_length=30, blank=False, default='', verbose_name='SKU Name')
    insurance_base_price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, default='', verbose_name='SKU Base Price')
    insurance_selling_price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, default='', verbose_name='SKU Selling Price')
    insurance_limit = models.PositiveIntegerField(validators=[MaxValueValidator(100),], blank=False, default='', verbose_name='SKU Limit')
    insurance_date_created = models.DateField(editable=False, default=date.today, verbose_name='SKU Date Created')
    insurance_days_covered = models.PositiveIntegerField(validators=[MaxValueValidator(365),], verbose_name='SKU Days Covered')
    insurance_age_start = models.PositiveIntegerField(validators=[MaxValueValidator(100),], verbose_name='SKU Age From')
    insurance_age_end = models.PositiveIntegerField(validators=[MaxValueValidator(100),], default='', verbose_name='SKU Age To')
    insurance_underwriter = models.ForeignKey(Underwriter)

    def __str__(self):
        return(self.insurance_name)

    class Meta:
        verbose_name = 'SKU'


class MicroInsuranceCompany(models.Model):
    micro_insurance_name = models.CharField(max_length=50, blank=False, default='', verbose_name='Micro Insurance Company Name')

    class Meta:
        verbose_name_plural = 'Micro Insurance Company'

    def __str__(self):
        return(self.micro_insurance_name)


class Position(models.Model):
    position_name = models.CharField(max_length=50, blank=True, default='', verbose_name='User Role')

    def __str__(self):
        return(self.position_name)

    class Meta:
        verbose_name = 'User Role'


class UserProfile(models.Model):
    username = models.CharField(max_length=50, blank=False, default='')
    password = models.CharField(max_length=50, blank=False, default='')
    user_firstname = models.CharField(max_length=50, blank=False, default='', verbose_name='First Name')
    user_middlename = models.CharField(max_length=50, blank=True, default='', verbose_name='Middle Name(optional)')
    user_lastname = models.CharField(max_length=50, blank=False, default='', verbose_name='Last Name')
    position_name = models.ForeignKey(Position, verbose_name='User Role')

    def __str__(self):
        return ''.join(
            [self.user_lastname,' ,', self.user_firstname, ' ', self.user_middlename])

    class Meta:
        verbose_name = 'User'


class Branch(models.Model):
    branch_name = models.CharField(max_length=50, blank=False, default='')
    branch_address = models.CharField(max_length=100, blank=False, default='')
    username = models.ForeignKey(UserProfile,verbose_name='Branch Manager')
    micro_insurance_name = models.ForeignKey(MicroInsuranceCompany, verbose_name='Micro Insurance Company')

    def __str__(self):
        return(self.branch_name)

    class Meta:
        verbose_name_plural = 'Branches'
 