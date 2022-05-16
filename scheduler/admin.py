from django.contrib import admin

from .models import Appointment, Patient, Staff, Doctor

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(Doctor)


