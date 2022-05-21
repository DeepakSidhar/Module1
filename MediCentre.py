def checkPassLong(length):
	if length >= 8 and length <=10 :
		print(checkPassUpper(password))
	else:
		return("Password is not within range")
	break

def checkPassUpper(password):
	upper_case_letters = [letter.isupper() for letter in password].count(True)
	if upper_case_letters >=1 :
		print(checkPassLower(password))
	else:
		return("Password does not have any capital")
	break



def checkPassLower(password):
	lower_case_letters = [letter.islower() for letter in password].count(True)
	if lower_case_letters >=1 :
		print("lower_case_letters", lower_case_letters)
		print(checkPassSpace(password))
	else:
		return("Password does not have any lower case")
		break

def checkPassSpace(password):
	for letter in password:
		if letter != " ":
			print("No Space ", )
			print(checkPassSpecial(password))
		else:
			print("space detected in password:")
			break

def checkPassSpecial(password):
	special = ['!', '@', '#', '$', '%', '&', '*']
	special_case_letters = 0
	for letter in password:
		if letter in special:
			special_case_letters +1
			print("Specail " , special_case_letters)


while(True):
	password = input("Please enter a Password  ")
	length =len(password)
	print("Please wait while we perform some checks !!")
	print("Total Length", length)
	print(checkPassLong(length))
	break

