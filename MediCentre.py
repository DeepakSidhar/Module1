#Import the Account class into main program
from Account import Account
#Import database
import data

def signup():
	#Create variable  user name and passeod
	username = input("Please enter a username  ")
	password = input("Please enter a password  ")
	print("Please wait while we perform some checks !!")
	#Create an account object  run the validate password - Hash the password then  add the account to the database
	account = Account(username, password)
	if account.validatePassword():
		account.hashPassword()
		data.addAccount(account)

def login():
	username = input("Please enter a username  ")
	password = input("Please enter a password  ")
	print("Please wait while we perform some checks !!")

	account = data.getAccountByUsername(username)

	if account == None:
		print("Please sign up!!")
	elif account.checkPassword(password):
		#Generating the token for the user
		print(f" your token is : {account.genToken()}")
		#Remove any space entered by the user
		token = input("Please enter the one time token:  ").strip()
		#IF the token match  by calling checkToken function then we grant access
		if account.checkToken(token):
			print("Login Sucessful")
		else:
			print(" Token mismatch.")
	else:
		print("Login credentials don't match ")

while True:
	print("Do you need to login or sign up")
	print("1 -login")
	print("2 -sign up")
	print("3 -database")

	command = input()

	if command.lower() == 'login' or command == '1':
		login()

	if command.lower() == 'signup' or command == '2':
		signup()

	if command.lower() == 'database' or command == '3':
		data.printDB()




