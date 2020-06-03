from rest_framework import serializers
from ClasseEtudiant import models
from django.contrib.auth import update_session_auth_hash

class EtudiantSerializers(serializers.HyperlinkedModelSerializer):
    num = serializers.CharField(required=True)
    prenom = serializers.CharField(required=True)
    nom = serializers.CharField(required=True)

    class Meta:
        model = models.Etudiant
        fields = ('id', 'num', 'prenom', 'nom')
        depth = 1

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return models.Etudiant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.num = validated_data.get('num', instance.num)
        instance.prenom = validated_data.get('prenom', instance.prenom)
        instance.nom = validated_data.get('nom', instance.nom)
        instance.save()
        return instance

class PromoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Promo
        fields = ('id', 'nomPromo', 'listeEtu')
        depth = 1
