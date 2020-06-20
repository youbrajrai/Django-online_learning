from django.contrib import admin
from .models import UserContactModel
# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
	list_display = ['name','email']
	search_fields = ['name']
admin.site.register(UserContactModel,ContactModelAdmin)