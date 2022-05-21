from django.urls import path

from . import views
#Base path /scheduler
# The below are in addition such as /scheduler/appointments/'
urlpatterns = [
	path('', views.index, name='index'), # This will show the views  of  hello world
	path('appointments/', views.list_appointments, name='list_appointments'),
	path('appointments/<int:appointment_id>', views.appointment_details, name='appointment_details'),
	path('appointments/create/', views.appointment_create, name='appointment_create'),


]