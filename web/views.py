from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FileCreationForm
from .models import File

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def file_form(request):
    return render(request, 'form.html', {'form': FileCreationForm})

def file_post(request):
    if request.method == 'POST':
        the_file = File(name=request.POST['name'], file=request.FILES['file'])
        the_file.save()
        return HttpResponseRedirect('/')

def file_view(request):
    return render(request, 'list.html', {})
