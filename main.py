from cryptography.fernet import Fernet


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'


def main():
    # master_pass = input("Please enter the Master Password :")
    # make_key()
    get_key()

    key = get_key()
    fern = Fernet(key)

    while True:
        operation = input(f" Would you like to : \n"
                          " 1. Add a new password\n"
                          " 2. View existing passwords\n"
                          " 3. Quit Password Manager\n"
                          "[Input 'Add' , 'View' or 'Quit']\n").lower()
        if operation == "quit":
            break
        elif operation == "add":
            add(fern)
            continue
        elif operation == "view":
            view(fern)
        else:
            print("Please select a valid operation")


def add(fern):
    credential_name = input("Please enter a nickname for your credentials i.e (Gmail Details)")
    username = input("Please enter your username : ")
    password = input("Please enter your password :")

    with open('passwords.txt', 'a') as f:
        f.write(credential_name + " | " + username + " | " + fern.encrypt(password.encode()).decode() + "\n")


def view(fern):
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            credential_name, username, password = data.split(" | ")
            print(f"{bcolors.HEADER}{bcolors.BOLD}{credential_name}{bcolors.ENDC}")
            print(f"{bcolors.BOLD}--------------{bcolors.ENDC}")
            print(f"{bcolors.OKBLUE}Username:{bcolors.ENDC} " + username)
            print(f"{bcolors.OKBLUE}Password:{bcolors.ENDC} " + fern.decrypt(password.encode()).decode() + "\n")


def make_key():
    key = Fernet.generate_key()
    with open('master_key.key', 'wb') as key_file:
        key_file.write(key)


def get_key():
    with open('master_key.key', 'rb') as file:
        return file.read()


if __name__ == '__main__':
    main()
