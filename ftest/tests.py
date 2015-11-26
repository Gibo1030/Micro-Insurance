from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InsuranceTest(StaticLiveServerTestCase):
    fixtures = ['admin_user.json'] #dumping data

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_log_in_admin(self):
        #admin page
        self.browser.get(self.live_server_url + '/admin/')

        #Django administration heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        insurance_links = self.browser.find_elements_by_link_text('Insurances')
        self.assertEquals(len(insurance_links), 1)

        insurance_links[0].click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('0 insurances', body.text)

        new_insurance_link = self.browser.find_elements_by_link_text('Add insurance')
        self.assertEquals(len(insurance_links), 1)
        new_insurance_link[0].click()

        #input fields
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Insurance name', body.text)
        self.assertIn('Insurance price', body.text)
        self.assertIn('Insurance limit', body.text)
        self.assertIn('Insurance date created', body.text)
        self.assertIn('Insurance validity start', body.text)
        self.assertIn('Insurance validity end', body.text)
        self.assertIn('Insurance age start', body.text)
        self.assertIn('Insurance age end', body.text)

        #insurance name test input
        insurance_name_field = self.browser.find_element_by_name('insurance_name')
        insurance_name_field.send_keys("Panaload10")

        #insurance price test input
        insurance_price_field = self.browser.find_element_by_name('insurance_price')
        insurance_price_field.send_keys('10.00')

        #insurance limit test input
        insurance_limit_field = self.browser.find_element_by_name('insurance_limit')
        insurance_limit_field.send_keys('3')

        #insurance date created
        insurance_date_created_field = self.browser.find_element_by_name('insurance_date_created')
        insurance_date_created_field.send_keys('11/26/15')

        #insurance validity
        insurance_validity_start_field = self.browser.find_element_by_name('insurance_validity_start')
        insurance_validity_start_field.send_keys('01/01/00')
        insurance_validity_end_field = self.browser.find_element_by_name('insurance_validity_end')
        insurance_validity_end_field.send_keys('01/01/01')

        #insurance age
        insurance_age_start_field = self.browser.find_element_by_name('insurance_age_start')
        insurance_age_start_field.send_keys('18')

        #save
        save_button = self.browser.find_element_by_css_selector("input[value='Save']")
        save_button.click()

        self.fail('Finish this test')