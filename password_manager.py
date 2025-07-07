from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key) '''

def load_key():
    file = open("key.key","rb")
    key_ = file.read()
    file.close()
    return key_

# master_pwd = input("What is the master password: ")
key = load_key() # + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            #print(line.rstrip())      #remove next black line
            data = line.rstrip()
            user,passw = data.split(" | ")   # pavan | killer | smile --> ['pavan', 'killer', 'smile']
            print("User:",user, "| Password:",fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('password.txt','a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() +"\n")
while True:
    mode = input("Would you like to add a new password or view existing ones(view) or Q to quit: ").lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue
