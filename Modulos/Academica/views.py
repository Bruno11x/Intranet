from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar(request):
    if request.method == 'POST':
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email" + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["Capacitatecherramientasdigital@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")

def home(request):
    return redirect('login')

def loginview(request):
    if request.method == 'POST':
        username = request.POST['Usuario']
        password = request.POST['Contraseña']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/admin/')
        else:
            return render(request, 'loginview.html', {'error': 'Invalid username or password'})
    return render(request, 'loginview.html')

def logoutview(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/admin/')