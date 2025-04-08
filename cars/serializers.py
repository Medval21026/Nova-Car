from rest_framework import serializers
from .models import *

class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'

class WilayeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaye
        fields = '__all__'

class MoughataaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moughataa
        fields = '__all__'

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class VoitureVenduSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoitureVendu
        fields = '__all__'

class VoitureLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoitureLocation
        fields = '__all__'

class SponsoriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsorise
        fields = '__all__'
        depth = 1