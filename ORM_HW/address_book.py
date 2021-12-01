from collections import UserDict
from datetime import timedelta, date, datetime
import re
import time

from sqlalchemy.sql.expression import insert,select
from queries import DBAddressBook


class Name:
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name.isalpha():
            self.__name = name
        else:
            print("Incorrect name!")

    def __str__(self):
        return f"{self.__name}"


class Phone:
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        if re.search("(^\+?(38)?0(44|67|68|96|97|98|50|66|95|99|63|73|93|89|94)\d{7}$)", re.sub(r'\D', "", phone)):
            if len(re.sub(r'\D', "", phone)) == 12:
                self.__phone = '+' + re.sub(r'\D', "", phone)
            else:
                self.__phone = '+38' + re.sub(r'\D', "", phone)
        else:
            print("The phone is not saved because it has an incorrect format\n"
                  "Try to edit like the example: +38(***)*******")

    def __str__(self):
        return f"{self.__phone}"


class Email:
    def __init__(self, email):
        self.__email = None
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if email == '-' or re.search("^[\w\.-]+@[\w\.-]+(\.[\w]+)+", email):
            self.__email = email
        else:
            print("The email is not saved because it has an incorrect format\n"
                  "Try to edit like the example: *****@***.***")

    def __str__(self):
        return f"{self.__email}"


class Birthday:
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        try:
            if birthday == '-' or time.strptime(birthday, '%d/%m/%Y'):
                self.__birthday = birthday
        except ValueError:
            print('The date is not saved because it has an incorrect format\n'
                  'Try to edit like the example: DD/MM/YYYY')

    def __str__(self):
        return f"{self.__birthday}"


class Address:
    def __init__(self, address):
        self.address = address
        self.__address = address

    def __str__(self):
        return f"{','.join(self.__address).title()}"


class Record:
    def __init__(self, name, phone, email, birthday, address):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.email = Email(email)
        self.birthday = Birthday(birthday)
        self.address = Address(address)

    def __str__(self):
        return f"{self.phone},{self.email},{self.birthday},{self.address}"


class AddressBook(UserDict):
    def add_record(self, name, phone, email, birthday, address):
        try:
            DBAddressBook.user_insert (lname=name, lphone=phone, lemail=email, lbirthday=birthday, laddress=address)
            print ('Contact is added')
        except Exception as error:
            print (f"Address hasn`t added {error}")


    def find_contact(self, name):
        try:
            DBAddressBook.user_select (name)
            
        except Exception as error:
            print (f"Address hasn`t found {error}")
         

    def del_contact(self, id):
        try:
            DBAddressBook.delete_record(id)
        except Exception as error:
            f"No such record"

    def edit_contact(self, id, name, phone, email, birthday, address):

        try:
            DBAddressBook.user_update(lid = id, lname=name, lphone=phone, lemail=email, lbirthday=birthday, laddress=address)
        except Exception as error:
            f"No such record"


    def days_to_birthday(self, number_days):
        EndDate = date.today() + timedelta(days=number_days)
        list = []
        try:
            for key, val in self.data.items():
                result = re.search(r"\d{1,2}\/\d{1,2}\/\d{4}", str(val)).group()
                if datetime.strptime(result, "%d/%m/%Y").month == EndDate.month \
                        and datetime.strptime(result, "%d/%m/%Y").day == EndDate.day:
                    list.append({str(key): str(val)})
        except AttributeError:
            pass
        return list

    def __str__(self):
        print(f'Total contacts: {len(self.data)}')
        for key, val in self.data.items():
            print(f'{str(key)}:{str(val)}'.removesuffix(','))