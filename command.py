from collections import UserDict

class AddressBook(UserDict):
    pass

class Contact:
    
    def __init__(self, *args):

        self.name = args[1]
        self.phone = args[2]
        #self.email = args[3]


class Record: 

    command_list = [
        "'add ...' - with this command I save a new contact. Instead of '...', enter the name and phone number, \nnecessarily separated by a 'space'.",
        "'change ... - with this command I save the new phone number of an existing contact. Instead of '...', \nenter the name and phone number, necessarily with a 'space'.",
        "'phone ....' - With this command, I output the phone number for the specified contact. Instead of '...' \nenter the name of the contact whose number should be displayed.",
        "'show_all' - With this command, I output all saved contacts with phone numbers.",
        "'good bye', 'close', 'exit' by any of these commands I complete my work."
    ]

    contact_list = []

    def hello(*args):

        print("    > How can I help you?! To find out the list of commands, write 'help'.")


    def print_command(self, *args):

        print("\n")

        for comm in self.command_list:
            print(f"    > {comm}\n")


    def new_contact(self, *args):

        

        self.contact_list.append(Contact(*args))
        print(f"    > You have added a new contact {args[1]}: {args[2]}.\n")
    

    def show_contact(self, *args):

        for i in r.contact_list:
            if i.name == args[1]:
                print(f'    > {i.name}: {i.phone}')
    

    def show_all(self, *args):

        for i in self.contact_list:
            print(f"    > {i.name}: {i.phone}\n")


    def change(self, *args):
        
        for i in self.contact_list:
            if i.name == args[1]:
                i.phone = args[2]
        
        print(f"    > You have updated the contact {args[1]}: {args[2]}.\n")


class Field:
    pass


class Name(Field):
    pass


class Phone(Field):
    pass


r = Record()

OPERATIONS = {
    "exit": ["exit", "close", "good bye"],
    "hello": r.hello, 
    "help": r.print_command,
    "add": r.new_contact,
    "phone": r.show_contact,
    "show_all": r.show_all,
    "change": r.change
}