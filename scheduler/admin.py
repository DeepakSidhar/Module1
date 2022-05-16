from django.contrib import admin

from .models import Appointment, Patient, Staff, Doctor, Admin, Nurse, Receptionist

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(Doctor)
admin.site.register(Admin)
admin.site.register(Nurse)
admin.site.register(Receptionist)


