from cryptography.fernet import Fernet

def load_key():
    
    #Loads the key from the current directory

    return open("key.key", "rb").read()

def decrypt(filename, key):

    #Decrypts the given file name with key
    
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    #Decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    #Write to original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


key = load_key()

file = "readme.txt"

decrypt(file, key)