from cryptography.fernet import Fernet

'''First 1) run the new file
2) press q in first run
3) Comment write_key() funtion and line
4) now run code and add pass and view pass
DONE!!
'''
def write_key():
    k = Fernet.generate_key()
    with open("key.key", "ab") as key_file:
        key_file.write(k)
write_key()

def load_key():
    file = open("key.key", "rb")
    k = file.read()
    file.close()
    return k


k = load_key()
fer = Fernet(k)


def view():
    with open('pas.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('pas.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


print("Thanks for using MAFIAPasMan\n\n")
pas = input("Enter a MasterKey: ")

if pas=='lenovo':
    while True:

        mode = input(
            "Choose one option (view, add), press q to quit? ").lower()
        if mode == "q":
            break

        if mode == "view":
            view()
            input()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
            continue
else:
    print("Bhag Bhosdike")
    input()
