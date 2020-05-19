from rest_framework import serializers
from user.models import *



class compte_Serializer(serializers.ModelSerializer):
    class Meta:
        model = compte
        fields = '__all__'


class reclamation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = reclamation
        fields = '__all__'
