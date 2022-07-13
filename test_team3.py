import unittest
from team3_pii import find_us_phone_numbers, find_us_ss_numbers, find_twitter_handles, find_email_addresses


class Team3TestCases(unittest.TestCase):
    def test_us_phone(self):
        # Test valid phone number
        phone = '336-555-1212'
        self.assertTrue(find_us_phone_numbers(phone))

        phone = '336.555.1212'
        self.assertTrue(find_us_phone_numbers(phone))

        phone = '(336)-575-1212'
        self.assertTrue(find_us_phone_numbers(phone))
        # Test invalid
        phone = 'My number is 336-42-1212'
        self.assertFalse(find_us_phone_numbers(phone))

    def test_ss_numbers(self):
        # Test valid ss number
        ss = "000-12-1234"
        self.assertTrue(find_us_ss_numbers(ss))

        ss = "020-40-0000"
        self.assertTrue(find_us_ss_numbers(ss))

        # Test invalid
        ss = "020-4-0000"
        self.assertFalse(find_us_ss_numbers(ss))

    def test_twitter_handles(self):
        # Test valid twitter handles
        twitter = "@john.jones"
        self.assertTrue(find_twitter_handles(twitter))

        twitter = "@james_j"
        self.assertTrue(find_twitter_handles(twitter))

        # Test invalid
        twitter = "@$james_#"
        self.assertFalse(find_twitter_handles(twitter))

    def test_email_addresses(self):
        # Test valid email addresses
        email = "john19jones@gmail.com"
        self.assertTrue(find_email_addresses(email))

        email = "jamestoocool777@yahoo.gov"
        self.assertTrue(find_email_addresses(email))

        # Test invalid
        email = "google.com"
        self.assertFalse(find_email_addresses(email))



if __name__ == '__main__':
    unittest.main()
