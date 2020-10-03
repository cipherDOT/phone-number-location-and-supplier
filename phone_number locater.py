import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate
# I also created a profile file to make this somewhat secure if you wanted to
from profile import username, password


def number_check(phone_number):
    number = phonenumbers.parse(phone_number)
    country = geocoder.description_for_number(number, 'en')
    supplier = carrier.name_for_number(number, 'en')
    info = [["Country", "Supplier"],[country, supplier]]

    return tabulate(info, headers = "firstrow", tablefmt = "textile")


if __name__ == '__main__':
    uname = input("Enter username: ")
    pword = input("Enter password: ")
    
    if uname == username and pword == password:
        number = input("Enter number(Enter full phone number): ")
        print(number_check(number))
