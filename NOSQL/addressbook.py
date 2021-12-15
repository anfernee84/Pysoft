from collections import UserDict
import mongofunctions

class AddressBook(UserDict):
    name = ''
    phone = ''
    email = ''
    address = ''
    def __init__ (self, name = '', phone = '', email = '', address = ''):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def add_record(self):
        try:
            mongofunctions.insert_document(name=self.name, phone=self.phone, email=self.email, address=self.address)
            print (f'A contact has been added')
        except Exception as error:
            print (f"A contact hasn`t been added {error}")


    def find_contact(self):
        try:
            result = mongofunctions.find_document(name = self.name)
            print (result)
        except Exception as error:
            print (f"Address hasn`t found {error}")
         

    def del_contact(self):
        try:
            mongofunctions.delete_document(name = self.name)
            print (f"contact {self.name} has been deleted")
        except Exception as error:
            f"No such record {error}"


    def edit_contact(self):
        try:
            mongofunctions.update_document (name=self.name, phone=self.phone, email=self.email, address=self.address)
            print(f"Contact {self.name} has been edited")
        except Exception as error:
            f"No such record {error}"

    def show_all():
        try:
            mongofunctions.select_all()
        except Exception as error:
            f"There are no records {error}"

