import os
import os.path

filename = 'UserList.txt'
mainfolder = 'C:\\Users\\user\\Desktop\\Codes\\Python Projects\\'\
                'Login System'

def NewUser():
    """For Creating a new user in the list"""
    username = input("Please Enter desired username: ")
    password, confpass = '', ' '
    username = CheckName(username) 
    print("Username available")     
    passmatch(password, confpass)     
    CreateUser(username, password)
    Createfolder(username)
    
def Createfolder(username):
        os.mkdir(username)
        print(f"Directory {username} created")
    
def CreateUser(username, pw):
    """Makes an ordered pair in the list file"""
    with open(filename, 'a') as file_object:
        file_object.write(f"{username}:{pw}\n")
        print("New User Created")

def CheckName(username):
    """For checking username availability and deconflict filename"""
    entries = os.listdir(mainfolder)
    for entry in entries:
        name, ext = os.path.splitext(entry)
        if name==username:
            username = input('Username already exists or is a'\
                                 'key file, enter a new one: ')
            CheckName(username)
    return username
    
def passmatch(password, checkpass):
    """Checks for matching password"""
    password = input("Please enter your password: ")
    password=strongpass(password)
    while password!=checkpass:
        checkpass = input("Please re-enter password: ")
        if password!=checkpass:
            print("Passwords do not match!")
            checkpass= ' '
            
def strongpass(password):
    """Makes sure password is strong"""
    if len(password)>=8 and \
        any(x.isupper() for x in password) and \
        any(x.islower() for x in password) and \
        any(x.isdigit() for x in password):
            pass
    else:
        password = input("Password not strong enough!\n"\
                            "Make sure you have one lowercase,"\
                            " one uppercase, one digit and more "\
                            "than 10 characters: ")
        password = strongpass(password)
    return password
    
def ExistingUser():
    """Allows existing users to log in"""
    username = input("Please enter your username: ")
    corrpass = CheckExisting(username)
    password = input("Please enter password: ")
    while password!=corrpass:
        password = input("Incorrect Password! Try Again: ")
    print("Access Granted")
    

def CheckExisting(username):
    """Checks to see if user exists"""
    with open(filename) as file_object:
        for line in file_object:
            user, pw = line.rsplit(':')
            if username==user:
                return pw.strip()
    username = input("No such user exists, re-enter username: ")
    CheckExisting(username)
        
    
if __name__=="__main__":
    newconf = input("Are you a new user? (y/n): ")
    
    if newconf=='y':
        NewUser()
        
    elif newconf=='n':
        ExistingUser()
            
            