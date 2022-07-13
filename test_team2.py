import unittest
from team2_pii import find_us_phone_numbers
from team2_pii import find_us_ssn
from team2_pii import find_credit_card_number

from team2_pii import find_us_email
from team2_pii import find_us_twitter_handle
from team2_pii import find_us_bank_account
from team2_pii import find_us_address


class Team2TestCases(unittest.TestCase):
    def test_us_phone(self):
        # Test valid phone number
        phone = '336-555-1212'
        self.assertTrue(find_us_phone_numbers(phone))

        phone = '336.555.1212'
        self.assertTrue(find_us_phone_numbers(phone))

        # Test invalid
        phone = 'My number is 336-42-1212'
        self.assertFalse(find_us_phone_numbers(phone))
    
    def test_us_ssn(self):
        # Test valid SSN
        ssn = '111-11-1111'
        self.assertTrue(find_us_ssn(ssn))

        ssn = '001-01-0001'
        self.assertTrue(find_us_ssn(ssn))

        # Test invalid SSN
        ssn = '000-00-0000'
        self.assertFalse(find_us_ssn(ssn))

        ssn = 'SSN: 123-456-7890'
        self.assertFalse(find_us_ssn(ssn))
    
    def test_credit_card_number(self):
        # Test valid credit card number
        ccn = '4444 4444 4444 4444' # Visa, Mastercard, Discover
        self.assertTrue(find_credit_card_number(ccn))

        ccn = '3333 333333 33333' # American Express
        self.assertTrue(find_credit_card_number(ccn))

        ccn = '5555-5555-5555-5555'
        self.assertTrue(find_credit_card_number(ccn))

        # Test invalid credit card number
        ccn = '1234'
        self.assertFalse(find_credit_card_number(ccn))

        ccn = 'hello'
        self.assertFalse(find_credit_card_number(ccn))

    def test_us_email(self):
        # Test emails
        email = 'tochah@freeallapp.com'
        self.assertTrue(find_us_email(email))

        email = '5464642@nakiuha.com'
        self.assertTrue(find_us_email(email))
        # invalid test
        email = 'jgfj4!3 @ gmail.com'
        self.assertFalse(find_us_email(email))

    def test_us_twitter(self):
        # Test Twitter Handles
        twt = "@junine12"
        self.assertTrue(find_us_twitter_handle(twt))
        # invalid test

        twt = "wenter"
        self.assertFalse(find_us_twitter_handle(twt))

        twt = "@17ds17__"
        self.assertTrue(find_us_twitter_handle(twt))

    def test_us_bank_account(self):
        # test bank account numbers. 8-12 digits long

        # valid numbers
        bank = '20392837'
        self.assertTrue(find_us_bank_account(bank))

        bank = '390948738903'
        self.assertTrue(find_us_bank_account(bank))

        # invalid accounts
        bank = '3452'
        self.assertFalse(find_us_bank_account(bank))

        bank = '345cn4nj3'
        self.assertFalse(find_us_bank_account(bank))

    def test_us_address(self):
        #testing valid address
        address = '5639 Havenville Street, Nashville, TN, 39448'
        self.assertTrue(find_us_address(address))

        address = '37621 Amber Street, Greensboro, NC, 39102-3914'
        self.assertTrue(find_us_address(address))

        #testing invalid address
        address = 'I live at 410335 Chamber Avenue, Phoenix, Arizona, 3018'
        self.assertFalse(find_us_address(address))

if __name__ == '__main__':
    unittest.main()
