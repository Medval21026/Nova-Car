from rest_framework import viewsets
from .models import *
from .serializers import *

class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

class WilayeViewSet(viewsets.ModelViewSet):
    queryset = Wilaye.objects.all()
    serializer_class = WilayeSerializer

class MoughataaViewSet(viewsets.ModelViewSet):
    queryset = Moughataa.objects.all()
    serializer_class = MoughataaSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class VoitureVenduViewSet(viewsets.ModelViewSet):
    queryset = VoitureVendu.objects.all()
    serializer_class = VoitureVenduSerializer

class VoitureLocationViewSet(viewsets.ModelViewSet):
    queryset = VoitureLocation.objects.all()
    serializer_class = VoitureLocationSerializer

class SponsoriseViewSet(viewsets.ModelViewSet):
    queryset = Sponsorise.objects.all()
    serializer_class = SponsoriseSerializer





from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_vendus(request):
    # Get all sold cars
    voitures_vendues = VoitureVendu.objects.filter(vendu=True)
    serializer = VoitureVenduSerializer(voitures_vendues, many=True)
    return Response(serializer.data)