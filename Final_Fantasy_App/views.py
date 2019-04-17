from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CharacterSerializer, PieceSerializer, DetailSerializer, WantedSerializer
from .models import Character, Gear_Details, GearPiece, WantedGear

# Create your views here.

class CharacterView(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class DetailView(viewsets.ModelViewSet):
    queryset = Gear_Details.objects.all()
    serializer_class = DetailSerializer

class PieceView(viewsets.ModelViewSet):
    queryset = GearPiece.objects.all()
    serializer_class = PieceSerializer

class WantedView(viewsets.ModelViewSet):
    queryset = WantedGear.objects.all()
    serializer_class = WantedSerializer