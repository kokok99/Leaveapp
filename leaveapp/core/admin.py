from django.contrib import admin
from .models import Application, Staff

# Register your models here.
class App(admin.ModelAdmin):

    #list of fields to display in django admin
    list_display = ['leave', 'date_created']

class Stff(admin.ModelAdmin):

    #list of fields to display in django admin
    list_display = ['fullname']


admin.site.register(Application, App)
admin.site.register(Staff, Stff)