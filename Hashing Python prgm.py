import hashlib as hlib
testhash = 0

print("    ________________________________________________________________________")
print(" ")
print("                          PASSWORD HASHING - PROJECT                      ")
print("    ________________________________________________________________________")
print(" ")
print(" ")
def hashing_fun(passwrd_hash):
    global testhash
    testhash = hlib.sha256(passwrd_hash.encode())
    print("Hash output: ",testhash.hexdigest())
    
def main():
    passwrd_hash = input("Enter your password: ")
    hashing_fun(passwrd_hash) 
    users_choice = input("Would you like to see if you have the right password? y/n : ").upper()
    if(users_choice == "Y"):
        hash_check()

def hash_check():
    users_pass = input("enter your password to test: ")
    users_hash = hlib.sha256(users_pass.encode())
    if(users_hash.hexdigest() == testhash.hexdigest()):
        print("Password confirmed")
        print("second password: ",users_hash.hexdigest())
        print("first password: ",testhash.hexdigest())
    else:
        print("Password is not the same")
        print("second password: ",users_hash.hexdigest())
        print("first password:  ",testhash.hexdigest())
        
main()
