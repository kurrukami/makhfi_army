from rest_framework import serializers
from annonce.models import *


class fiche_Serializer(serializers.ModelSerializer):
    class Meta:
        model = fiche_annonce
        fields = '__all__'




class Ad_Serializer(serializers.ModelSerializer):
    fiche = fiche_Serializer()
    class Meta:
        model = annonce_demande
        fields = '__all__'
        depth = 0
    def create(self, validated_data):
        return annonce_demande.objects.create(**validated_data)

class Ao_Serializer(serializers.ModelSerializer):
    fiche = fiche_Serializer()
    class Meta:
        model = annonce_offrir
        fields = '__all__'


class Av_Serializer(serializers.ModelSerializer):
    fiche = fiche_Serializer()
    class Meta:
        model = annonce_ville
        fields = '__all__'


class L_Serializer(serializers.ModelSerializer):
    fiche = fiche_Serializer()
    class Meta:
        model = livraison
        fields = '__all__'
