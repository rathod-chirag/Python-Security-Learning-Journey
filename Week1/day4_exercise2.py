# Exercise 2 : Contact Book

# 1. Add contact.
def add_contact(filename,name,phone,email):

    new_contact = f"{name},{phone},{email}\n"
    
    with open(filename,'a') as f:
        try:
            f.write(new_contact)
            print("Contact Saved!")
        except ValueError as e:
            print(f"Error: {e}")
    

# 2. View All contact.
try:
    def view_contacts(filename):
        """View all contacts"""
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        if not lines:
            print("\n📭 No contacts yet!")
            return
        
        print("\n" + "="*70)
        print("ALL CONTACTS")
        print("="*70)
        print(f"{'Name':<20} {'Phone':<15} {'Email':<30}")
        print("-"*70)
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) >= 3:
                print(f"{parts[0]:<20} {parts[1]:<15} {parts[2]:<30}")
        
        print("="*70)
except FileNotFoundError:
    print("No contact yet!")
except Exception as e:
    print(f"Error: {e}")
    
# 3. search contact.
def search_contact(filename,search):
     
    with open(filename,'r') as f:
        try:
            found = False
            for line in f:
                line = line.strip()
                if not line:
                    continue

                contact = line.split(',')
                if contact[0] == search:
                        print("Contact Found.")
                        print(f"Name: {contact[0]}")
                        print(f"Phone: {contact[1]}")
                        print(f"Email: {contact[2]}")
                        found = True
                        return
        except FileNotFoundError:
            print("No contacts file found!")
                
    if not found:
            print(f"\n Contact '{search}' not found")  

    


# 4. delete contact      
def delete_contact(filename,name):
    with open(filename,'r') as f:
        lines = f.readlines()

        remaining = []
        found = False

        for line in lines:
            line = line.strip()
            if not line:
                continue

            contact = line.split(',')
            if contact[0] == name:
                found = True
            else:
                remaining.append(line + '\n')
        
        with open(filename,'w') as f:
            try:
                f.writelines(remaining)
            except FileNotFoundError:
                print("No contacts to delete.")
        
        if found:
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")
                    
                

# def update_contact(filename,name,new_phone,new_email):

# Menu
def contact_menu(filename):
    try:
        while True:
            print("\n"+"="*40)
            print("CONTACT MENU:")
            print("="*40)
            print("1. Add conntact.")
            print("2. View conntacts.")
            print("3. Search conntact.")
            print("4. Delete conntact.")
            print("5. Exit")
            print("="*40)
            
            choice = int(input("Enter choice (1-5)"))


            if choice == 1:
                name = input("Enter the name: ")
                phone = input("Enter the phone no.: ")
                email = input("Enter the email: ")

                if name.strip():
                    raise ValueError("Name cannot be empty")
                
                if not name:
                    raise ValueError("Name cannot be empty.")
    
                if not phone.isdigit():
                    raise ValueError("Number contains only digits")
        
                if len(phone) != 10:
                    raise ValueError("Phone number must of 10 digits.")
        
                if '@' not in email:
                    raise ValueError("Invalide email.")
                
                add_contact(filename,name,phone,email)

            elif choice == 2:
                view_contacts(filename)

            elif choice == 3:
                search = input("Enter the name to search: ")
                search_contact(filename,search)

            elif choice == 4:
                search = input("Enter the name to delet contact: ")
                delete_contact(filename,search)

            elif choice == 5:
                print("Thank you for using Contact Book")
                break
            else:
                print("Invalide choice! Please enter 1-5.")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Exiting..")
        



filename  =  'contact.txt'


contact_menu(filename)






