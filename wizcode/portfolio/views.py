from contextlib import redirect_stderr
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import ContactForm
from . import models
from django.contrib import auth, messages
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    return render(request, 'index.html')

def contact_form(request):
    return render(request, 'index.html')

def contactView(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        a = models.Contact(full_name = full_name, email = email, subject=subject, message=message)
        a.save()
        messages.success(request, "Message Sent Successfully, I'ld get back to you")
        return redirect('home')
    else:
        messages.error(request, 'Message Sent Fail, try again later')
        return redirect('contact_form')

class ProjectListView(ListView):
    model = models.Project
    template_name = 'index.html'
    context_object_name = 'projects'
    paginate_by = 6
    
    def get_queryset(self):
        return models.Project.objects.order_by('-id')
