from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)


def view():
    with open ("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            try:
                user, passw = data.split("|")
                decrypted_password = fer.decrypt(passw.encode()).decode()
                print("User:", user, "| Password:", decrypted_password)
            except Exception as e:
                print(f"Error decrypting password for {user}: {e}")

def add():
    user_name = input("Account name: ")
    pwd = input("Password: ")

    with open ("passwords.txt", "a") as f:
        f.write(user_name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones. Press q to quit? (Add/ View)? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
    