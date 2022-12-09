
# CPSC 329 GROUP PROJECT (PASSWORD MANAGER)
A simple easy to use python application used to store randomly generated passwords for the user.

# Project Objective:
To create a comprehensive password manager from scratch using Python and Tkinter to allow users to create and 
store multiple passwords and login information from one safe space.

# Program Description:

The user will be able to access the program through a master password, 
where random passwords can be generated, or simply stored for multiple websites. 
With the help of a hashing algorithm, the user will be able to securely store strong passwords in fingerprint form, 
in a place where they can be easily accessed.

# Created Program - Expected Program Functionality:
- The start of the program will prompt the user to create a master password. This password will be stored as the user’s key to allow the addition, removal, and viewing of passwords
- The program will give the option for the user to add a password. Adding a password prompts the user to enter a website or program name to associate the password with.
    - This creates a random password string containing lower and uppercase letters, special characters, and numbers.
    - This is then stored with the corresponding website name as a fingerprint, using a hashing algorithm.
- The program will give the option for the user to remove a password. This action asks for the website name and then deletes the fingerprint for the desired website location.
- The program will give the option to view a list of all passwords. This will display a list of all fingerprints in their encoded form.
- The program will give the user the option to view the password of a specific website. This will display the password of a specific website in decoded form.
- A functional GUI will be created via Tkinter, to allow for ease of use. This will include options to perform any of the above functions.

# Frontend and Backend:

- Frontend 
    - We used python's Tkinter library to make a functional GUI 
    - It provides a fast and easy way to create GUI applications
    - Importing tkinter is same as importing any other module in the Python code. Note that the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x it is ‘tkinter’.
         ```python
        import tkinter 
        ```
- Backend 
    - To store the user passwords, we make use of the hasing algorithm called sha256.
        -   SHA-256 stands for Secure Hash Algorithm 256-bit and it’s used for cryptographic security.
            Cryptographic hash algorithms produce irreversible and unique hashes. The larger the number of possible hashes, the smaller the chance that two values will create the same hash.
        - Why Hashing?
            - Hashing is irreversible and unidirectional.
            - The original message cannot be retrieved.
            - The resultant hash is of fixed length.
            - Purpose of hashing is to ensure data integrity.
            
    - To implement the hasing we simply make use of the hashlib library in python   
       ```python
        import hashlib
        ```
        - we enode the password first in utf-8 and then hash it
    - For storing the passwords we make use of sqlite3 To use sqlite3 module, you must first create a connection object that represents the database and then optionally you can create a cursor object, which will help you in executing all the SQL statements.
- How it works?
    - The user first creates a masterpassword which is then hased and stored into the database
    - The user then is redirected to the password manager where he can then start storing the passwords
    - The user can then close and run the program after which he will be redirected to the login page where he will have to enter the masterpassword he created 
    - The hash of the entered password is then compared with hash stored into the database and then the access is granted again 



## Deployment

- To deploy this project
    - You will need to have Python 3 or above to run 
    - You will also need to have the necessary pyhton packages downloaded
    

# Screenshots of the Program:-

![Screen Shot 2022-12-08 at 6 16 49 PM](https://user-images.githubusercontent.com/91339174/206603665-6842e457-48a6-483d-9d56-30e3baf0d0b5.jpg)


![Screen Shot 2022-12-08 at 6 17 25 PM](https://user-images.githubusercontent.com/91339174/206603738-d0f7e194-b628-4000-ad1a-ccd96a45618d.jpg)


![Screen Shot 2022-12-08 at 6 17 56 PM](https://user-images.githubusercontent.com/91339174/206603780-303866e7-aa46-4c74-a073-35d4234aba1a.jpg)

## Authors

- [@aniruddha-10](https://github.com/aniruddha-10)
- [@darrenkeilty](https://github.com/darrenkeilty)
- [@SohaibbS](https://github.com/SohaibbS)
- [@TG74](https://github.com/TG74)

