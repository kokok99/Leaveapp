from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('dashboard/', views.index, name= 'dashboard'),
    path('calendar/', views.calendar, name= 'calendar'),
    path('form/', views.form, name='form'),
    path('dashboard/view/<int:pk>/', views.viewapp, name='view'),
    path('history_view/<int:pk>/', views.history_view, name='h_view'),
    path('dashboard/delete/<int:pk>/', views.delete, name='delete'),
    path('staff_delete/<int:pk>/', views.staff_delete, name='staff_delete'),
    path('staff_view/<int:pk>/', views.staff_view, name='staff_view'),
    path('print/<int:pk>/', views.print, name='print'),
    path('history', views.history, name='history'),
    path('staff_profile', views.staff, name='profile-staff'),
    path('staff_profile/<int:pk>/', views.staff_profile, name='staff_profile'),
    path('edit_staff/<int:pk>/', views.edit_staff, name='edit_staff_details'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('pending/', views.pending, name='pending'),
    path('csv/', views.getdata, name='csv'),
]