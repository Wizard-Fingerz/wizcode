from django.forms import ModelForm
from portfolio.models import Contact
from dataclasses import field
from django import forms



class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("full_name", "email", "subject", "message",)