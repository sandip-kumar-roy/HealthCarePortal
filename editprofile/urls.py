from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('profile_base', views.profile_base,name='profile_base'),
    path('edit_profile', views.edit_profile,name='edit_profile'),
    path('delete_prof', views.delete_prof,name='delete_prof'),
    path('change_pass', views.edit_profile_password,name='change_pass'),
]