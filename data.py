import Account
from typing import List
#This is creating an empty in memory database array.
#Please note once the app is stopped the data is lost.
database = []

#Getters and setters

#If user name matches we will return  username
def getAccountByUsername(username:str) -> Account:
	for account in database:
		if account.username == username:
			return account


#Added data into the  database
def addAccount(account: Account):
	database.append(account)


def printDB():
	for account in database:
		print(account)