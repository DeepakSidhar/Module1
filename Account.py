#import bycrpt
import bcrypt

class Account:
	#Attributes of the class
	username: str
	password: str

	#Constructor taking in the paramters username and passoword and setting the attributes above
	def __init__(self, username, password):
		self.username = username
		self.password = password


	def checkPassLong(self):
		if len(self.password) >= 8 and len(self.password) <=10 :
			return True
		else:
			print("Password is not in range")
			return False

	def checkPassUpper(self):
		for letter in self.password:
			if letter.isupper():
				return True
		print("No upper case Characters in password:")
		return False


	def checkPassLower(self):
		for letter in self.password:
			if letter.islower():
				return True
		print("No lower case Characters in password:")
		return False

	def checkPassSpace(self):
		for letter in self.password:
			if letter == " ":
				print("space detected in password:")
				return False

		return True

	def checkPassSpecial(self):
		special = ['!', '@', '#', '$', '%', '&', '*']
		for letter in self.password:
			if letter in special:
				return True
		print("No special  characters in password:")
		return False

	def validatePassword(self):
		return self.checkPassUpper() \
		       and self.checkPassLower() \
		       and self.checkPassSpace() \
		       and self.checkPassSpecial()

	def hashPassword(self):
		#The below is eenerating a encode bit hash password and salt.
		hash = bcrypt.hashpw(str.encode(self.password), bcrypt.gensalt())
		self.password = hash.decode()

	def checkPassword(self, password):
		return bcrypt.checkpw(str.encode(password), str.encode(self.password))

	def __str__(self):
		return self.username + '-->' + self.password