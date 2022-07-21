# PII: files/november_statement.pdf: Name: John Smith
# NO_PII: files/november_statement.pdf: MyBank.com - Banking Statement
from scan import get_file_text, scan_files
from team1_pii import find_us_phone_numbers, find_us_street_address, find_twitter_handle, find_credit_card_number, \
    find_bank_acc_number, find_email_address


def find_pii(text):
    detected_pii_list = []

    if find_us_phone_numbers(text):
        detected_pii_list.append('us_phone_number')

    if find_us_street_address(text):
        detected_pii_list.append('us_street_address')

    if find_twitter_handle(text):
        detected_pii_list.append('twitter_handle')

    if find_credit_card_number(text):
        detected_pii_list.append('credit_card_number')

    if find_bank_acc_number(text):
        detected_pii_list.append('bank_acc_number')

    if find_email_address(text):
        detected_pii_list.append('email_address')

    return detected_pii_list


def main():
    # get list of files to be scanned
    file_list = scan_files()
    for f in file_list:
        # get the text from the file
        for text in get_file_text(f):
            result = find_pii(text)
            if result:
                # PII was found
                print(': '.join(['PII', f, text]))
                print(result)
            else:
                # No PII found in this file
                print(': '.join(['NO_PII', f, text]))


if __name__ == '__main__':
    main()
