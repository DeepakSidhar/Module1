#import bycrpt.Kislyuk(n.d.)
import bcrypt
#import pyotp. bcrypt 3.2.2 (May 02, 2022)
import pyotp
#import base64.How to Base64 Encode a String in Python (July 21. 2021)
import base64

class Account:
#Attributes of the class.
	username: str
	password: str
	token: pyotp.TOTP

#Constructor taking in the paramters username, password and token and setting the attributes above.
	def __init__(self, username, password):
		self.username = username
		self.password = password
		#Make use of base64 to handle type error.
		self.token = pyotp.TOTP(base64.b32encode(b"Hello This is MediCentre" + bytearray(self.username, "ascii")))

#Check the password length is between equal to 8 and abouve characters  but less than  or equale 10.
	def checkPassLong(self):
		if len(self.password) >= 8 and len(self.password) <=10 :
			return True
		else:
			print("Password is not in range")
			return False

#Check the password provided one upper case.
	def checkPassUpper(self):
		for letter in self.password:
			if letter.isupper():
				return True
		print("No upper case Characters in password:")
		return False

#Check the password provided one lower case.
	def checkPassLower(self):
		for letter in self.password:
			if letter.islower():
				return True
		print("No lower case Characters in password:")
		return False

#Check the password provided does not contain a space.
	def checkPassSpace(self):
		for letter in self.password:
			if letter == " ":
				print("space detected in password:")
				return False

		return True

#Check the password provided contains a special character.
	def checkPassSpecial(self):
		special = ['!', '@', '#', '$', '%', '&', '*']
		for letter in self.password:
			if letter in special:
				return True
		print("No special  characters in password:")
		return False

#This function is envoked by the main MediCentre program when a user is signing up. To ensure the password meet the abouve requirments.
	def validatePassword(self):
		return  self.checkPassLong() \
		and self.checkPassUpper() \
		and self.checkPassLower() \
		and self.checkPassSpace() \
		and self.checkPassSpecial()

#This functuon uses the bcrypt library and  hashes the password  provided by the user
	def hashPassword(self):
		#The below is generating hash password and salt.
		hash = bcrypt.hashpw(str.encode(self.password), bcrypt.gensalt())
		self.password = hash.decode()

#This functuon uses the bcrypt library and  checks  the password and hashed password
	def checkPassword(self, password):
		return bcrypt.checkpw(str.encode(password), str.encode(self.password))

	def __str__(self):
		return self.username + '-->' + self.password

#This functuon uses the one Time Password and generates a token with the username
	def genToken(self):
		return self.token.now()

#This functuon verfies the one Time Password
	def checkToken(self, token):
		return self.token.verify(token)




