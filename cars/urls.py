from django.contrib import admin
from django.urls import include, path
from . import mobile, views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('voiture_vendu', views.voiture_vendu, name='voiture_vendu'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)