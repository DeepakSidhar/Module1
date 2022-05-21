#Import the Account class into main program
from Account import Account

while True:
	#Create variable  user name and passeod
	username = input("Please enter a username  ")
	password = input("Please enter a password  ")
	print("Please wait while we perform some checks !!")
	#Create an account object  called a
	a = Account(username, password)
	a.validatePassword()


