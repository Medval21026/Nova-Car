from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Inscription(models.Model):
    login = models.CharField(max_length=100, unique=True)
    mot_de_passe = models.CharField(max_length=128)

class Wilaye(models.Model):
    code_wilaye = models.IntegerField(primary_key=True)
    nom_wilaye_Ar = models.CharField(max_length=255, blank=True, null=True)
    nom_wilaye_fr = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.nom_wilaye_Ar

class Moughataa(models.Model):
    nom_fr = models.CharField(max_length=255)
    nom_ar = models.CharField(max_length=255)
    wilaye = models.ForeignKey(Wilaye, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom_ar

class Utilisateur(models.Model):
    nom_ar = models.CharField(max_length=100)
    prenom_ar = models.CharField(max_length=100)
    nom_fr = models.CharField(max_length=100)
    prenom_fr = models.CharField(max_length=100)
    numero_telephone = models.CharField(max_length=20)
    password = models.CharField(max_length=128, null=True, blank=True)
    photo_de_profile = models.ImageField(upload_to='profils/', blank=True, null=True)
    wilaye = models.ForeignKey('Wilaye', on_delete=models.CASCADE)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE, default=None)



class VoitureVendu(models.Model):
    TRANSMISSION = [
        ('Automatique', 'Automatique'),
        ('Manuelle', 'Manuelle'),
    ]

    CARBURANT = [
        ('Essence', 'Essence'),
        ('Gazoil', 'Gazoil'),
    ]

    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION)
    carburant = models.CharField(max_length=20, choices=CARBURANT)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)
    distance = models.CharField(max_length=50,default="0")
    description = models.TextField(blank=True, null=True)  

    # 5 images
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='imagaes/', blank=True, null=True)
    image4 = models.ImageField(upload_to='imagaes/', blank=True, null=True)
    image5 = models.ImageField(upload_to='images/', blank=True, null=True)

    vendu = models.BooleanField(default=False)

class VoitureLocation(models.Model):
    TRANSMISSION = [
        ('Automatique', 'Automatique'),
        ('Manuelle', 'Manuelle'),
    ]

    CARBURANT = [
        ('Essence', 'Essence'),
        ('Gazoil', 'Gazoil'),
    ]

    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.IntegerField()
    prix_journalier = models.DecimalField(max_digits=10, decimal_places=2)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION)
    carburant = models.CharField(max_length=20, choices=CARBURANT)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)

    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='images/', blank=True, null=True)

    disponible = models.BooleanField(default=True)
    duree_minimale = models.IntegerField(default=1)  # Ajout du champ entier (ex: durée min de location)
    description = models.TextField(blank=True, null=True)  
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # Position GPS
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # Position GPS



def get_first_voiture_vendu():
    return VoitureVendu.objects.first()


class Sponsorise(models.Model):
    voiture = models.ForeignKey(VoitureVendu, on_delete=models.CASCADE,default=get_first_voiture_vendu )
    date_debut = models.DateField()
    date_fin = models.DateField()
    actif = models.BooleanField(default=True)