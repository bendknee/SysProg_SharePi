from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .forms import FileCreationForm
from .models import File
import subprocess

# Create your views here.

granted_access = []
waiting_access = []

def index(request):
    from ipware import get_client_ip
    ip, is_routable = get_client_ip(request)
    ip = ip.replace(".","")
    if(ip in granted_access):
        return render(request, 'index.html', {})
    elif(ip not in waiting_access):
        waiting_access.append(ip)
        subprocess.check_output("qr --factory=pymaging " + ip + " > web\\\static\\\images\\\qrcode.png", shell=True)
    return render(request, 'index.html', {"file":"qrcode.png"})

def file_form(request):
    return render(request, 'form.html', {'form': FileCreationForm})

def file_post(request):
    if request.method == 'POST':
        the_file = File(name=request.POST['name'], file=request.FILES['file'])
        the_file.save()
        return HttpResponseRedirect('/')

def file_view(request):
    return render(request, 'list.html', {})

def request_access(request):
    code = request.GET["code"]
    if(code in  waiting_access):
        granted_access.append(code)
        waiting_access.remove(code)
        response = {"status" : "success"}
    else:
        response = {"status" : "failed"}
    return JsonResponse(response)