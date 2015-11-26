from django.db import models
from datetime import date

class Insurance(models.Model):
    insurance_name = models.CharField(max_length=50, blank=False, default='Default')
    insurance_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default='0')
    insurance_limit = models.CharField(max_length=10, blank=False, default='0')
    insurance_date_created = models.DateField(default=date.today)
    insurance_validity_start = models.DateField(default=date.today)
    insurance_validity_end = models.DateField(default=date.today)
    insurance_age_start = models.IntegerField(default='0')
    insurance_age_end = models.IntegerField(default='0')
    insurance_underwriter = models.ForeignKey('Underwriter')

class Underwriter(models.Model):
    underwriter_name = models.CharField(max_length=50, blank=False, default='Default')

    def __str__(self):
        return(self.underwriter_name)