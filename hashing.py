import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

salt = os.urandom(16)


class PasswordManager:

    def __init__(self):
        # key object. Later generated by PBKDF2 key derivation function
        self.key = None
        # random value to salt passwords
        self.salt = None
        # filepath to where the password dictionary is stored.
        self.pwd_file = None
        # dictionary to store passwords.
        self.pwd_dict = {}

    """
    Function to generate a new master key via PBKDF2 key derivation function, and a random salt value.
    Stores new key and salt value in separate files. 
    """

    def derive_master_key(self, password):
        self.salt = salt
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=self.salt, iterations=10000)            # not sure what iterations are, value might need to be larger
        self.key = kdf.derive(password.encode("utf-8"))     # not sure if encoding to utf-8 works here. Otherwise can't write to the file though, not sure why.
        with open("key.txt", 'wb') as f:                    # it would be better to store these in a database, rather than in files within the project path.
            f.write(self.key)                               # but tricky to figure out. Might just have to mention this in our project overview.
        with open("salt.txt", 'wb') as f:
            f.write(self.salt)

    """
    Function to load a previously created key.
    """

    def load_key(self, filepath):                           # not finished, would have to decode as well probably
        with open(filepath, 'rb') as f:
            self.key = f.read().decode("utf-8")

    def new_pwd_file(self, filepath):                       # this is if the file to store passwords doesnt already exist
        self.pwd_file = filepath

    def load_pwd_file(self, filepath):                      # this would load the password dictionary
        self.pwd_file = filepath
        with open(filepath, 'r') as f:
            for i in f:
                x = 0
