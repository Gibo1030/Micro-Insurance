from django.test import TestCase
import datetime
from micro_insurance.models import Insurance

class InsuranceModelTest(TestCase):

    def test_creating_a_new_insurance_saving_to_the_database(self):
        insurance = Insurance()
        insurance.insurance_name = 'Panaload10'
        insurance.insurance_price = '10'
        insurance.insurance_limit = '3'
        insurance.insurance_date_created = datetime.date.today()
        insurance.insurance_days_covered = '30'
        insurance.insurance_age_start = '12'
        insurance.insurance_age_end = '60'

        insurance.save()

        all_insurance_in_database = Insurance.objects.all()
        self.assertEquals(len(all_insurance_in_database), 1)
        only_insurance_in_database = all_insurance_in_database[0]
        self.assertEquals(only_insurance_in_database, insurance)

        self.assertEquals(only_insurance_in_database.insurance_name, 'Panaload10')
        self.assertEquals(only_insurance_in_database.insurance_price, 10)
        self.assertEquals(only_insurance_in_database.insurance_limit, '3')
        self.assertEquals(only_insurance_in_database.insurance_date_created, insurance.insurance_date_created)
        self.assertEquals(only_insurance_in_database.insurance_days_covered, 30)
        self.assertEquals(only_insurance_in_database.insurance_age_start, 12)
        self.assertEquals(only_insurance_in_database.insurance_age_end, 60)
