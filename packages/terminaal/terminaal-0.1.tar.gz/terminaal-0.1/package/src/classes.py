from collections import UserDict
from datetime import datetime
from .birthdays import get_birthdays_per_week, get_birthdays_by_days
from .validate import name_is_valid, phone_is_valid, date_is_valid, email_is_valid
import re


class Field:
    """Represents a field to be filled"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Represents the contact`s name"""

    def __init__(self, value):
        if name_is_valid(value):
            self.value = value.title()
        else:
            raise NameError("Name should starts with letter")


class Phone(Field):
    """Represents the contact`s phone number"""

    def __init__(self, value):
        if phone_is_valid(value):
            self.value = value
        else:
            raise ValueError("Phone should be 10 digits format")


class Email(Field):
    """Represents the contact`s email"""

    def __init__(self, value):
        if email_is_valid(value):
            self.value = value
        else:
            raise ValueError("Invalid email format")


class Birthday(Field):
    """Represents the contact`s birthday"""

    def __init__(self, value: str):
        if date_is_valid(value):
            try:
                self.value = datetime.strptime(value, "%d.%m.%Y").date()
            except ValueError as e:
                raise ValueError("Invalid date value: " + str(e))
        else:
            raise ValueError("We couldn't validate entered date. Please, try again")


class Address(Field):
    """Represents the contact`s address"""

    def __init__(self, street, house_number, city, postal_code=None, country=None):
        self.street = street
        self.house_number = house_number
        self.city = city
        self.postal_code = postal_code
        self.country = country

    def __str__(self):
        address_parts = [self.street, self.house_number, self.city]
        if self.postal_code:
            address_parts.append(self.postal_code)
        if self.country:
            address_parts.append(self.country)
        return ", ".join(address_parts)


class Note(UserDict):
    """Represents a note with title, text and tags"""

    def __init__(self, title, text, tags):
        super().__init__()
        self.data["title"] = title
        self.data["text"] = text
        self.data["tags"] = tags

    def __str__(self):
        return f"{'=' * 50}\nTitle: {self.data['title']}\nText: {self.data['text']}\nTags: {' '.join(self.data['tags'])}"


class Record:
    """Represents a contact in your address book"""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.birthday = None
        self.addresses = []
        self.emails = []
        self.money = 0

    def add_phone(self, value):
        self.phones.append(Phone(value))

    def add_email(self, value):
        self.emails.append(Email(value))

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, phone, new_phone):
        found = False
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone
                print(f"Phone {phone} was changed to {new_phone}.")
                found = True
        if not found:
            raise IndexError(f"Phone {phone} wasn't found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value

    #
    def add_birthday(self, value):
        self.birthday = Birthday(value)
        return "birthday added"

    def __str__(self):
        if self.birthday == None:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value.strftime('%d.%m.%Y')}"

    def add_address(self, street, house_number, city, postal_code=None, country=None):
        self.addresses.append(Address(street, house_number, city, postal_code, country))

    def edit_address(self, street, house_number, city, postal_code=None, country=None):
        if self.addresses:
            address = self.addresses[0]
            if street:
                address.street = street
            if house_number:
                address.house_number = house_number
            if city:
                address.city = city
            if postal_code:
                address.postal_code = postal_code
            if country:
                address.country = country
            return "Address edited."
        else:
            return "No address to edit."

    def remove_address(self):
        self.addresses = []

    def deposit(self, amount):
        self.money += amount

    def withdraw(self, amount):
        self.money -= amount


class AddressBook(UserDict):
    """Represents an address book"""

    def __init__(self, name="contacts"):
        super().__init__()
        self.name = name

    def __dict__(self):
        return {"name": self.name, "records": dict(self.data)}  # Restructure for JSON

    def add_record(self, record):
        self.data[record.name.value] = record
        # print(f'Added new record: "{record}"')

    def find(self, value):
        for name, record in self.data.items():
            if name == value:
                return record
            else:
                raise IndexError(f"Record for {value} wasn't found")

    def delete(self, name):
        try:
            key_for_delete = None
            for key in self.data.keys():
                if key == name:
                    key_for_delete = key
            self.data.pop(key_for_delete)
            print(f"{name}'s contact was deleted")
        except KeyError:
            print(f"{name}'s contact wasn't found")

    def get_birthdays_per_week(self):
        """Shows you people who are going tot celebrate their birthday in the next seven days"""
        users = []
        for name, record in self.data.items():
            if record.birthday != None:
                users.append({"name": name, "birthday": record.birthday.value})
        return get_birthdays_per_week(users)

    def get_birthdays_by_days(self, days):
        """Shows you people who are going tot celebrate their birthday in the certain amount of days"""
        users = []
        for name, record in self.data.items():
            if record.birthday != None:
                users.append(
                    {
                        "name": name,
                        "phones": record.phones,
                        "birthday": record.birthday.value,
                    }
                )
        return get_birthdays_by_days(users, days)
