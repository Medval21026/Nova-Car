from django.shortcuts import render
from django.views import View
from .models import Inscription

def login(request):
    if request.method == 'POST':
        login_value = request.POST.get('login')
        mot_de_passe = request.POST.get('pwd')

        try:
            inscription = Inscription.objects.get(login=login_value)
            if check_password(mot_de_passe, inscription.mot_de_passe):
                return redirect('page_acceuil')
            else:
                error_message = "Login or password is incorrect."
                return render(request, 'pages/login.html', {'error_message': error_message})

        except Inscription.DoesNotExist:
            error_message = "Login or password is incorrect."
            return render(request, 'pages/login.html', {'error_message': error_message})
    return render(request, 'pages/login.html')

def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'pages/home.html')
def voiture_vendu(request):
    return render(request, 'pages/voiture vendu/voiture_vendu.html')