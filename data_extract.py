import re

def extract_emails(text):
    return re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

def extract_urls(text):
    return re.findall(r'https?://[^\s]+', text)

def extract_phone_numbers(text):
    return re.findall(r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}', text)

def extract_credit_cards(text):
    return re.findall(r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}', text)

def extract_times(text):
    return re.findall(r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b(?:\s?[APMapm]{2})?', text)

def main():
    try:
        with open('test_data.txt', 'r', encoding='utf-8') as file:
            content = file.read()

        print("Extracted Data ===============")
        print("Emails:", extract_emails(content))
        print("URLs:", extract_urls(content))
        print("Phone Numbers:", extract_phone_numbers(content))
        print("Credit Cards:", extract_credit_cards(content))
        print("Times:", extract_times(content))

    except FileNotFoundError:
        print("Error: File not found in the current directory.")

if __name__ == "__main__":
    main()