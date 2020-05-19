from rest_framework import serializers
from annonce.models import *



class Ad_Serializer(serializers.ModelSerializer):
    class Meta:
        model = annonce_demande
        fields = '__all__'


class Ao_Serializer(serializers.ModelSerializer):
    class Meta:
        model = annonce_offrir
        fields = '__all__'


class Av_Serializer(serializers.ModelSerializer):
    class Meta:
        model = annonce_ville
        fields = '__all__'


class L_Serializer(serializers.ModelSerializer):
    class Meta:
        model = livraison
        fields = '__all__'


class fiche_Serializer(serializers.ModelSerializer):
    class Meta:
        model = fiche_annonce
        fields = '__all__'
