from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email',)
    ordering = ('contact_name',)
    search_fields = ('contact_name', 'contact_email',)