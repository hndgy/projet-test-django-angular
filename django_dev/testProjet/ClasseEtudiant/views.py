from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from ClasseEtudiant import models
from ClasseEtudiant import serializers
from rest_framework import viewsets

# Create your views here.


class EtudiantViews(viewsets.ModelViewSet):
    """
    retourne la liste des Questionnaires
    """
    queryset = models.Etudiant.objects.all()
    serializer_class = serializers.EtudiantSerializers

class PromoViews(viewsets.ModelViewSet):
    """
    retourne la liste des question
    """
    queryset = models.Promo.objects.all()
    serializer_class = serializers.PromoSerializers
