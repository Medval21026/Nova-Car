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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VoitureVendu
from .serializers import VoitureVenduSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_vendus(request):
    # Get all sold cars
    voitures_vendues = VoitureVendu.objects.filter(vendu=True)
    serializer = VoitureVenduSerializer(voitures_vendues, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_count(request):
    # Get all sold cars
    voitures_etat_vendues = VoitureVendu.objects.filter(vendu=True).count()
    vendus_total = VoitureVendu.objects.all().count()
    location_total = VoitureLocation.objects.all().count()
    return Response({"vendus": voitures_etat_vendues, "vendus_total": vendus_total, "location_total": location_total})

 


class AjouterVoitureVendu(APIView):
    def post(self, request, format=None):
        serializer = VoitureVenduSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("adding car failed : ",serializer.errors)
        print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AjouterVoitureLocation(APIView):
    def post(self, request, format=None):
        serializer = VoitureLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("adding car failed : ",serializer.errors)
        print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)