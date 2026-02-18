# Exercise 1: Simple Logger.

from datetime import datetime

def write_log(massege,filename):
    log_entry = f"[{timestamp}] {massage}\n"
    with open(filename,'a') as f:
        f.write(log_entry)
        print("Log Saved!")

def view_logs(filename):
    with open(filename,'r') as f:
        logs = f.read()
        print(logs)

def clear_logs(filename):
    with open(filename,'r') as f:
        data = f.read()
        if data :
            with open(filename,'w') as f:
                print("Logs Cleared!")
        else:
            print("Cancelled!")
    


nows = datetime.now()
timestamp = nows.strftime("%Y-%m-%d %H:%M:%S")
print(timestamp)
massage = input("Enter the Massage: ")
filename = 'log.txt'
write_log(massage,filename)
view_logs(filename)
Per = input("Are you sure? (Yes/No)")
if Per.lower() == 'yes':
    clear_logs(filename)
elif Per.lower() == 'no':
    print("Logs are not cleared!")
else:
    print("Invalide Input.")

