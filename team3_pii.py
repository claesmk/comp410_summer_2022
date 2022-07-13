from scan import scan_files, get_file_text
import re


# https://developers.google.com/edu/python/regular-expressions
# https://regex101.com/
def find_us_phone_numbers(text):
    match = re.search(r'(\(\d{3}\)[-.]\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})', text)
    if match:
        return True
    return False


def find_us_ss_numbers(text):
    match = re.search(r'(\d{3}-\d{2}-\d{4})', text)
    if match:
        return True
    return False


def find_twitter_handles(text):
    match = re.search(r'(\@[a-zA-Z\d_.]+)', text)
    if match:
        return True
    return False


def find_email_addresses(text):
    match = re.search(r'([a-zA-Z\d[0-9]+@[a-zA-Z]+\.[(com|edu|gov)]+)', text)
    if match:
        return True
    return False
