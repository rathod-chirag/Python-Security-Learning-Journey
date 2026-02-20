import random
import string
from datetime import datetime

# Generate Password
def generate_password(length = 12, use_special = True, use_number = True):

    character = string.ascii_letters

    if use_special:
        character = character + string.punctuation

    if use_number:
        character = character + string.digits

    password = ''.join(random.choice(character) for _ in range(length))

    return password


# Check Password Stength
def check_password_strength(password):
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        pass

    if any(c.islower() for c in password):
        score += 1
    
    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score >= 5:
        print("Strong! ")
    elif score >= 3:
        print("Medium! ")
    else:
        print("Weak!")


# Save the password
def save_passsword(service,password):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        entry = f"{service},{password},{timestamp}\n"

        with open("password.txt","a") as f:
            f.write(entry)
            print("Password Saved ! ")
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    

# View All Passwords
def view_all_password():
    try:
        with open('password.txt','r') as f:
            lines = f.readlines()

            if not lines:
                print("No Password Saved Yet!")
                return
            
            print("="*60)
            print("SAVED PASSWORDS")
            print("="*60)

            print(f"{"Service":<20} {"Password":<15} {"TimeStamp"}")

            for line in lines:
                line = line.strip()

                if not line:
                    continue
                
                pas = line.split(",")

                service = pas[0]
                password = pas[1]
                time = pas[2]

                print(f"{service:<20} {password:<15} {time}")

            print("="*60)

    except FileNotFoundError:
        print("No Password Yet!")
    except Exception as e:
        print(f"Error: {e}")


# Search for specific password
def search_password(service_name):
    try:
        with open("password.txt",'r') as f:
            found = False

            lines = f.readlines()

            for line in lines:

                info = line.strip().split(",")

                if service_name == info[0]:
                    print(f"{info[0]:<20} {info[1]:<15} {info[2]}")
                    found = True
                    return
                
            if not found:
                print("Not Found!")
            

    except FileNotFoundError:
        print("File Not Found!")
    except Exception as e:
        print(f"Error: {e}")
    

# Delete Password specific password.

def delete_password(service_name):
    try:
        with open('password.txt','r') as f:
            lines = f.readlines()
            remaining = []

            found = False

            for line in lines:
                line = line.strip()
                info = line.split(",")

                if service_name == info[0]:
                    found = True
                else:
                    remaining.append(line)

            with open('password.txt','w') as f:
                for line in remaining:
                    f.write(line+"\n")
                    
            
        if found:
            print("Deleted Successfully!")
        else:
            print("Password Not Found!")
    except FileNotFoundError:
        print("File Not Found!")
    except Exception as e:
        print(f"Error: {e}")


# Main Menu to access the Password Manager.
def main_menu():
    while True:

        print("="*70)
        print("PASSWORD MANAGER")
        print("="*70)

        print("1. Generate New Password.")
        print("2. View All Password.")
        print("3.Search Password.")
        print("4.Delete Password.")
        print("5. Check Password Strength.")
        print("6. Exit")

        print("="*70)

        choice = int(input("Enter the choice Number to do the task(1-6)."))

        try:
            if choice == 1:

                length = int(input("Enter the password length to generate password: "))
                special = input("Do you want a special charecters in the password (yes/no): ")
                numbers = input("Do you want a digits in the password (yes/no): ")

                sp = False
                nu = False

                if special == 'yes':
                    sp = True

                if numbers == 'yes':
                    nu = True

                new_pass = generate_password(length,use_special=sp,use_number=nu)
                print(f"Generated Password: {new_pass}")
                check_password_strength(new_pass)
                save = input("Do you want to save the passsword(yes/no): ")

                if save.lower() == 'yes':
                    service = input("Enter the service name : ")
                    save_passsword(service,new_pass)

            elif choice == 2:
                view_all_password()
            elif choice == 3:
                ser = input("Enter the service name: ")
                search_password(ser)
            elif choice == 4:
                ser = input("Enter the service name: ")
                con = input("Do you really want to delet password(yes/no): ")
                if con.lower() == 'yes':
                    delete_password(ser)
                else:
                    pass
            elif choice == 5:
                pas = input("Enter the password to check Strength: ")
                check_password_strength(pas)
            elif choice == 6:
                print("Goodbye!")
                break
            else:
                print("Invalide Choice! Enter vaalide choice(1-6)")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main_menu()

                    



