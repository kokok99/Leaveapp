from dataclasses import fields
from email.mime import application
import django_filters
from .models import Application

class AppFilter(django_filters.FilterSet) :

    class Meta:
        model = Application
        fields = {'leave' : ['exact']}