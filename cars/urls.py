from django.contrib import admin
from django.urls import include, path
from . import mobile, views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .mobile import *

# Initialize router
router = DefaultRouter()
router.register(r'api/inscriptions', InscriptionViewSet)
router.register(r'api/wilayes', WilayeViewSet)
router.register(r'api/moughataas', MoughataaViewSet)
router.register(r'api/utilisateurs', UtilisateurViewSet)
router.register(r'api/voitures_vendues', VoitureVenduViewSet)
router.register(r'api/voitures_location', VoitureLocationViewSet)
router.register(r'api/sponsorises', SponsoriseViewSet)

 


urlpatterns = [
    path('', include(router.urls)),  
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('voiture_vendu', views.voiture_vendu, name='voiture_vendu'),
























    



    # ******************************************************************* mobile urls *******************************************************************
    path('VoituresVendu_status_vendu', get_vendus, name='get_vendus'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)