from django.http import HttpResponse
from django.http import Http404

# This is importing the templates files
from django.shortcuts import render, get_object_or_404
from .models import Appointment


# Create your views here.

def index(request):
	x = 50
	#return HttpResponse("Hello, world. You're at the scheduler index. and the value of the X is " + str(x))
	context = { 'x' : x }
	return render(request, 'scheduler/index.html', context)

def list_appointments(request):
	#TODO get the list of all the appointments from db
	appointment_list = Appointment.objects.all()
	context = {
		'appointment_list': appointment_list,
		'no_of_appointments':len(appointment_list)
	}
	return render(request, 'scheduler/appointment_list.html', context)

def appointment_details(request, appointment_id): # This is getting the url request and appointment ID from the url also
	#TODO get the list of all the appoimtnets from DB
	#PK is the primary key
	appointment = get_object_or_404(Appointment, pk = appointment_id)
	context = {'appointment': appointment}
	return render(request, 'scheduler/appointment_details.html', context)

def appointment_create(request): # This is getting the url request  from the url also
	print('Rendering create appointment')
	return render(request, 'scheduler/appointment_create.html')