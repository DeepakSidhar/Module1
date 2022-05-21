from django.db import models

# Create your models here.
#Call Appointment extends model.Model

class Patient(models.Model):
	SEX = {
		('male', 'MALE'),
		('female', 'FEMALE'),
		('others', 'OTHERS'),
	}
	#patientID = models.IntegerField()  Provided by DjangoForeign Keys
	#name  = models.CharField(max_len)   Provided by DjangoForeign Keys
	address = models.CharField(max_length = 500)
	contact = models.CharField(max_length = 500)
	age = models.PositiveIntegerField()
	sex = models.CharField(max_length = 50, choices = SEX)



class Staff(models.Model):
	#staffID: int
	#name = models.CharField(max_length = 500) Provided by DjangoForeign Keys
	#surname = models.CharField(max_length = 500) Provided by DjangoForeign Keys
	address = models.CharField(max_length = 500)
	contact = models.CharField(max_length = 500)
	department = models.CharField(max_length = 500)
	#roleID = models.IntegerField() django has roles

class Doctor(Staff):#Doctor extends staff.
	speciality = models.CharField(max_length = 500)
	qualification = models.CharField(max_length = 500)

#As the below have nothing we set them to pass.
class Admin(Staff):
	pass

class Nurse(Staff):
	pass

class Receptionist(Staff):
	pass

# created a asppoimtent class with type fields defined
class Appointment(models.Model):
	dateTime = models.DateTimeField()
	#appointmentID = models.IntegerField()#  Provided by DjangoForeign Keys
	# one doctor can handle one appoint
	# we need to ensure we have relation bewtween the tables in the DB
	doctor = models.OneToOneField(
		Doctor,
		on_delete=models.CASCADE, # delete all  assoication with  doc as  in appointment.
	)

	patient = models.OneToOneField(
		Patient,
		on_delete=models.CASCADE, # delete all  assoication with  doc as  in appointment.
	)

	symptoms = models.CharField(max_length = 500)# This is to ensure we can have multipe String
	diagnosis = models.CharField(max_length = 50)




