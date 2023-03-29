from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

def administador(request): #url is /login
    return render(request, 'administrador.html')