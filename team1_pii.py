from scan import scan_files, get_file_text
import re


# https://developers.google.com/edu/python/regular-expressions
# https://regex101.com/
def find_us_phone_numbers(text):
    match = re.search(r'(\d{3}[-.]\d{3}[-.]\d{4})', text)
    if match:
        return True
    return False

def find_us_street_address(text):
    match = re.search(r'(\d{1,4}\s{1}[a-zA-z\s]*,\s{1}[a-zA-z\s-]*,\s{1}[A-Z]{2},\s{1}(\d{5}-\d{4}|\d{5}))', text)
    if match:
        return True
    return False

def find_credit_card_number(text):
    match = re.search(r'\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}', text)
    if match:
        return True
    return False

def find_twitter_handle(text):
    match = re.search(r'\B@\w*([A-Za-z0-9_]+)\w*', text)
    if match:
        return True
    return False
