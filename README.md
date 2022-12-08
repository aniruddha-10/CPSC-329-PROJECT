# CPSC-329-PROJECT

## Final Project Introduction - Password Manager

Password managers are helpful in that they keep all user passwords in a single secure location. This allows the user to develop strong passwords that they do not have to remember while maintaining overall security. 
				          	                            
## Main Goal of the Project-
The following project is developed to materialize the concept of a password manager. As a general definition, password managers are programs used to store and access user credentials. By employing this program, users can dedicate a single master password to access all other passwords they choose to store. In this way, the program developed is like a password bank, where user login information can be stored securely, and accessed conveniently through the created GUI.


The strength of a password can be determined by a number of factors, and NIST helpfully lists a few. By their guidelines, passwords should have both length and complexity requirements. So typically, password strength can be assessed by the following attributes:
The length of a password
The presence of uppercase characters
The presence of lowercase characters
The presence of numeric characters
The presence of a keyboard special character or symbol

Throughout the following developed program, any password that a user wishes to use must meet the above conditions, where, the password must have a minimum length of 10, and each of the above character types is included at least once. In this way, the program ensures that each password entered is objectively strong, and in turn, difficult to crack.

The program also offers an option for a randomly generated password to be stored, where the resulting password is even stronger. The random generation function procedurally adds printable characters to a password string, until it reaches a length of 20. The strength conditions above are then checked to ensure that the generated password meets each requirement. So, through the use of this algorithm, the user can otto use a strong, random password that will be extremely difficult to crack.   







Users can use this program to manage their accounts and passwords on different websites and applications. At the time of registration, various conditions are placed on the format and composition of the master account password to ensure information security.
Passwords are stored in non-plaintext form after adding will hashing, we chose to use sha265, the advantage because the only way to get the same hash value is to enter the same file or string. Even a small tweak can completely change the output, and sha256 is a deterministic one-way hash function, so sha256 is irreversible


## Contributors:		
Darren Keilty
Tianyi Gao
Aniruddha Khan
Sohaib Sahid

