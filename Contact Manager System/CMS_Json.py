import json


contact_file = "Contacts.json"
def load_contacts():
    try:
        with open(contact_file, 'r') as file:
            contacts = json.load(file)
            return contacts
    except:
        contacts = []
        with open(contact_file, 'w') as file:
            json.dump(contacts, file, indent=4)
        return contacts

def add_contact():
    contacts = load_contacts()
    view_all_contacts()
    print("To Add new Contact fill the details below!")
    name = input("Enter Name: ")
    phone = input("Enter Phone number: ")
    email = input("Enter Email Address: ")
    contact = {"Name":name, "Phone": phone, "Email": email}
    contacts.append(contact)
    with open(contact_file, 'w') as file:
        json.dump(contacts, file, indent=4)
    view_all_contacts()
def view_all_contacts():
    contacts = load_contacts()
    print("List of Stored Contacts\n", 39*"-")
    for i in range(len(contacts)):
        contact = contacts[i]
        print(f"{1+i}", "Name:", contact["Name"], "| Phone:", contact["Phone"], "| Email:", contact["Email"])
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
                    contact = contacts[i]
                    if contact_search in contact["Name"].lower() or  contact_search in contact["Phone"].lower() or contact_search in contact["Email"].lower():
                        print(f'{i+1}. "Name:", {contact["Name"]}, "| Phone:", {contact["Phone"]}, "| Email:", {contact["Email"]}')
                
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
            contact_index = int(input("Enter Contact Number you want to Update or 0 to Exit: "))

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
                with open(contact_file, 'w') as file:
                    json.dump(contacts, file, indent=4)

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
                with open(contact_file, 'w') as file:
                    contacts.pop(contact_index-1)
                    json.dump(contacts, file, indent=4)
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