My proposed solution is to implement a secure password policy, Store an encrypted password in the database and  also generate a One Time Password (OTP), which will give the user a 30-second window to enter the token,

The main app is MediCentre.py, which prompts the user if they would like to log in, Sign up, or database. The login option checks if the username is available in the database. If the account is not present, the user will need to sign up. If present, then the password is checked against the encrypted password, and if matched successfully, able to log in otherwise rejected.

The Sign-up option performs several verifications on the password and ensures it contains a minimum of 8 characters and a maximum of 10 characters. The characters must include a minimum of one uppercase and one lowercase and contain special characters such as !, @, #, $, %, &,*  The password must ensure there is no space.

The database option is for the demo of this exercise to show a hashed password is stored and needs to be removed. 