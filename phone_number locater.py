import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder


def number_check(phone_number):
    number = phonenumbers.parse(phone_number)
    description = geocoder.description_for_number(number, 'en')
    supplier = carrier.name_for_number(number, 'en')
    info = [description, supplier]
    return info

