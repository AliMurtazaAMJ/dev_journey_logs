import sqlite3



conecter = sqlite3.connect("Contacts.db")

Pointer  = conecter.cursor()

Pointer.execute("""
    CREATE TABLE IF NOT EXISTS Contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    Name TEXT NOT NULL, 
    Phone TEXT NOT NULL, 
    Email TEXT NOT NULL
    )

""")


def load_contacts():
    
    Pointer.execute('Select * from Contacts')
    contacts = Pointer.fetchall()
    return contacts

def add_contact():
    view_all_contacts()
    print("To Add new Contact fill the details below!")
    name = input("Enter Name: ")
    phone = input("Enter Phone number: ")
    email = input("Enter Email Address: ")
    Pointer.execute('INSERT INTO Contacts(Name, Phone, Email ) values (?, ?, ?)', (name, phone, email, ))
    conecter.commit()
    view_all_contacts()
def view_all_contacts():
    contacts = load_contacts()
    print("List of Stored Contacts\n", 39*"-")
    for i in contacts:
        
        print(f" {i}")

    print(40*"-")

def search_contact():
    view_all_contacts()
    while True:
        contacts = load_contacts()
        try: 
            contact_search = input("Enter your Search Quiry or 0 to Exit: ").lower()
            if contact_search == "0":
                break
            if 0 < len(contact_search):
                    
                for i in range(len(contacts)):
                    Pointer.execute("SELECT * FROM Contacts WHERE name LIKE ?", (contact_search,))
                else:
                        print("No Results Found!")
                
                
            else:
                print("Please Enter a valid Quiry!")
        except Exception as e:
            print(e)

def update_contact():
    view_all_contacts()
    while True:
        contacts = load_contacts()
        try: 
            contact_index = int(input("""Enter Contact Number you want to Update or 0 to Exit: """))

            if 1 <= contact_index <= len(contacts): 
                name = input("Enter New Name or Enter: ")
                phone = input("Enter New Phone or Enter: ")
                email = input("Enter New Email or Enter: ")
                
                if len(name) != 0:
                    contacts[contact_index-1]["Name"] = name
                if len(phone) != 0:
                    contacts[contact_index-1]["Phone"] = phone
                if len(email) != 0:
                    contacts[contact_index-1]["Email"] = email
                
                view_all_contacts()
                break
            elif contact_index == 0:
                break
            else:
                print("Please Enter a valid Delete contact Option")
        except Exception as e:
            print(e)


def delete_contact():
    view_all_contacts()
    contacts = load_contacts()
    while True:
        try: 
            contact_index = int(input("Enter Contact Number you want to Delete or 0 to Exit: "))
            if 1 <= contact_index <= len(contacts): 
                Pointer.execute('DELETE FROM Contacts where id = ?', (contact_index,))
                conecter.commit()
                view_all_contacts()
                break
            elif contact_index == 0:
                break
            else:
                print("Please Enter a valid Delete contact Option")
        except Exception as e:
            print(e)


    




def main():
    print("CLI Base Contact Manager System!\n", 45*"=")
    option = input("""Select the Option you want to perform!
    1. Add contact
    2. View all contacts
    3. Search contact
    4. Update contact
    5. Delete contact\n
Select the Option: """)
    if option == "1":
        add_contact()
    elif option =="2":
        view_all_contacts()
    elif option =="3":
        search_contact()
        
    elif option == "4":
        update_contact()
    elif option =="5":
        delete_contact()
    elif option =="0":
        exit()
    else:
        print("Please Select a valid Option!")

while True: 
    main()