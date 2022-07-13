from scan import scan_files, get_file_text
import re


# https://developers.google.com/edu/python/regular-expressions
# https://regex101.com/
def find_us_phone_numbers(text):
    match = re.search(r'(\d{3}[-.]\d{3}[-.]\d{4})', text)
    if match:
        return True
    return False


def find_twitter_usernames(text):
    match = re.search(r'\B@\w*([A-Za-z0-9_]+)\w*', text)
    if match:
        return True
    return False


def find_email_handle(text):
    match = re.search(r'^([^.@]+)(\.[^.@]+)*@([^.@]+\.)+([^.@]+)$', text)
    if match:
        return True
    return False


def find_credit_card_numbers(text):
    visa_mastercard_discover = r'\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}'  # Visa, Mastercard, Discover
    amex = r'\d{4}[- ]\d{6}[- ]\d{5}'  # American Express
    diners = r'\d{4}[- ]\d{6}[- ]\d{4}'  # Diners Club

    match = re.search('^(' + visa_mastercard_discover + '|' + amex + '|' + diners + ')$', text)
    if match:
        return True
    return False

def find_account_number(text):
    match = re.search(r'^(\d{3,12})$', text)

    if match:
        return True
    return False
