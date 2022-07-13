import unittest
from team4_pii import find_us_phone_numbers, find_twitter_usernames, find_email_handle, find_credit_card_numbers, find_account_number


class Team4TestCases(unittest.TestCase):
    def test_us_phone(self):
        # Test valid phone number
        phone = '336-555-1212'
        self.assertTrue(find_us_phone_numbers(phone))

        phone = '336.555.1212'
        self.assertTrue(find_us_phone_numbers(phone))

        # Test invalid
        phone = 'My number is 336-42-1212'
        self.assertFalse(find_us_phone_numbers(phone))

    def test_twitter_usernames(self):
        # Test valid usernames
        twitterHandle = '@ncatsuaggies'
        self.assertTrue(find_twitter_usernames(twitterHandle))

        twitterHandle = '@FatKidDeals01'
        self.assertTrue(find_twitter_usernames(twitterHandle))

        twitterHandle = '@CNN_sports'
        self.assertTrue(find_twitter_usernames(twitterHandle))

        # Test invalid usernames
        twitterHandle = 'CNN'
        self.assertFalse(find_twitter_usernames(twitterHandle))

        twitterHandle = 'google@'
        self.assertFalse(find_twitter_usernames(twitterHandle))

    def test_credit_card_numbers(self):
        # Test Valid Cards
        visa_mastercard_valid = '4012 8888 8888 1881'
        self.assertTrue(find_credit_card_numbers(visa_mastercard_valid))

        amex_valid = '3782 822463 10005'
        self.assertTrue(find_credit_card_numbers(amex_valid))

        diners_valid = '3782 822463 0005'
        self.assertTrue(find_credit_card_numbers(diners_valid))

        # Test Invalid Cards
        visa_mastercard_invalid = '4111 1111 1111 111'
        self.assertFalse(find_credit_card_numbers(visa_mastercard_invalid))

        amex_invalid = '3782 82243 10005'
        self.assertFalse(find_credit_card_numbers(amex_invalid))

        diners_invalid = '3782 82463 0005'
        self.assertFalse(find_credit_card_numbers(diners_invalid))
        
    def test_email_address(self):
        # valid email
        valid_email_1 = 'mail@gmail.com'
        self.assertTrue(find_email_handle(valid_email_1))
        
        # valid email
        valid_email_2 = 'mail @ apple . com'
        self.assertTrue(find_email_handle(valid_email_2))
        
        # invalid email
        invalid_email_1 = 'mail@apple.'
        self.assertFalse(find_email_handle(invalid_email_1))
        
        # invalid email
        invalid_email_2 = '@apple.com'
        self.assertFalse(find_email_handle(invalid_email_2))
        

    def test_account_number(self):
        # Test valid account numbers
        accountnumber = '1235489652'
        self.assertTrue(find_account_number(accountnumber))

        accountnumber = '52489'
        self.assertTrue(find_account_number(accountnumber))

        accountnumber = '954129'
        self.assertTrue(find_account_number(accountnumber))

        # Test invalid accountnumbers
        accountnumber = '12'
        self.assertFalse(find_account_number(accountnumber))

        accountnumber = '0002547893124d'
        self.assertFalse(find_account_number(accountnumber))


if __name__ == '__main__':
    unittest.main()
