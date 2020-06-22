from django.urls import path
from .views import login,register,contact_register,logout
app_name = 'registration'
urlpatterns = [
	path('contact_register/',contact_register,name='contact_register'),
	path('login/',login,name='login'),
	path('logout/',logout,name='logout'),
	path('register/',register,name='register'),
]