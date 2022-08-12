from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.ProjectListView.as_view(), name = 'home'),
    path('contact_form/', views.contact_form, name="contact_form"),
    path('contact', views.contactView, name='contact'),
    
]