from django.shortcuts import render, redirect
from .models import Info, Experience, Project
from .forms import ContactForm
from .send_email import send_email
# Create your views here.
def index(request):
    info = Info.objects.last()
    experience1 = Experience.objects.all().order_by('-created_at')[0:2]
    experience2 = Experience.objects.all().order_by('-created_at')[2:4]
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'info/index.html', {'info': info, 'experience1': experience1,
            'projects': projects, "experience2": experience2})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_email(form.cleaned_data.get('name'), form.cleaned_data.get('email'), form.cleaned_data.get('message'))
            return redirect('/')
        else:
            return redirect('/')
    else:
        redirect('/')