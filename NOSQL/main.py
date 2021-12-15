import addressbook

def main():
    print(f"Welcome to your personal assistant!\nI can add\delete\change and show you some notes\n")

    while True:
        try:
            cmd = input("What should i do?:").lower()
            sep_cmd = cmd.split(" ")
            if sep_cmd[0] == "add" and sep_cmd[1] == "contact":
                abook = addressbook.AddressBook (sep_cmd[2].title(),
                                                    sep_cmd[3],
                                                    sep_cmd[4] if len(sep_cmd) > 4 else "--",
                                                    sep_cmd[5] if len(sep_cmd) > 5 else "--")
                abook.add_record()

            elif sep_cmd[0] == "show" and sep_cmd[1] == "contact":
                abook = addressbook.AddressBook (sep_cmd[2].title())
                abook.find_contact()

            elif sep_cmd[0] == "show" and sep_cmd[1] == "all":
                addressbook.AddressBook.show_all()

            elif sep_cmd[0] == "edit" and sep_cmd[1] == "contact":
                abook = addressbook.AddressBook (sep_cmd[2].title(), sep_cmd[3],  sep_cmd[4], sep_cmd[5])
                abook.edit_contact()
                
            elif sep_cmd[0] == "delete" and sep_cmd[1] == "contact":
                print (sep_cmd[2].title())
                abook = addressbook.AddressBook(sep_cmd[2].title())
                abook.del_contact()
            
            elif cmd in ["quit", "close", "exit"]:
                print("Thank you for using our software! Good bye!")
                break
             
        
        except Exception as error:
            f"Input incorrect {error}"
    

if __name__ == "__main__":
    main()