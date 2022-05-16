from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'), # This will show the views  of  hello world
]