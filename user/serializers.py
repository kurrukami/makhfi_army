from rest_framework import serializers
from user.models import *
from annonce.models import *


class reclamation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = reclamation
        fields = '__all__'




class compte_Serializer(serializers.ModelSerializer):
    class Meta:
        model = compte
        fields = '__all__'
        extra_kwargs = {
                    'password' : {'write_only' : True}
        }
