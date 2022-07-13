from scan import scan_files, get_file_text
import re


# https://developers.google.com/edu/python/regular-expressions
# https://regex101.com/
def find_us_phone_numbers(text):
    match = re.search(r'(\d{3}[-.]\d{3}[-.]\d{4})', text)
    if match:
        return True
    return False

def find_us_ssn(text):
    match = re.search(r'([0-9]{2}[1-9]|[0-9][1-9][0-9]|[1-9][0-9]{2})[-\s]([0-9][1-9]|[1-9][0-9])[-\s]([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]|[0-9][1-9][0-9]{2}|[1-9][0-9]{3})', text)
    if match:
        return True
    return False

def find_credit_card_number(text):
    match = re.search(r'([0-9]{4}[- ][0-9]{4,6}[- ][0-9]{4,5}[- ]?[0-9]{0,4})', text)
    if match:
        return True
    return False
def find_us_twitter_handle(text):
    match = re.search(r'^[@](\w){1,15}$', text)
    if match:
        return True
    return False

def find_us_email(text):
    match = re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', text)
    if match:
        return True
    return False

def find_us_bank_account(text):
    match = re.search(r'^(\d{8,12})$', text)
    if match:
        return True
    return False

def find_us_address(text):
    match = re.search(r'(\d{1,5}\s{1}[\w\s]*,\s{1}[\w\s-]*,\s{1}[A-Z]{2},\s{1}(\d{5}-\d{4}|\d{5}))', text)
    if match:
        return True
    return False
