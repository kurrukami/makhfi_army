from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from django.conf import settings

from rest_framework.authtoken.models import Token
# Create your views here.


def haveItOrNot(request, obj):
    user = request.auth
    print(user)
    if obj.compte != user:
        return Response({"warnning ...denided_response":"im callig FBI ,u dont have permission u sob "})
    else:
        perm = 11
        return perm





def which_one(request, type):
    user = request.auth
    if type == "AD":
        t_many = annonce_demande.objects.all()
        s_many = Ad_Serializer(t_many, many=True)
        s_post = Ad_Serializer(user, data=request.data)
        return {"objects" : t_many, "serializer_many" : s_many, "serializer_one" : s_one, "serializer_post" : s_post}

    elif type == "AO":
        t_many = annonce_offrir.objects.all()
        s_many = Ao_Serializer(t_many, many=True)
        s_post = Ao_Serializer(user, data=request.data)
        return {"objects" : t_many, "serializer_many" : s_many, "serializer_one" : s_one, "serializer_post" : s_post}

    elif type == "L":
        t_many = livraison.objects.all()
        s_many = L_Serializer(t_many, many=True)
        s_post = L_Serializer(user, data=request.data)
        return {"objects" : t_many, "serializer_many" : s_many, "serializer_one" : s_one, "serializer_post" : s_post}

    elif type == "AV":
        t_many = annonce_ville.objects.all()
        s_many = Av_Serializer(t_many, many=True)
        s_post = Av_Serializer(user, data=request.data)
        return {"objects" : t_many, "serializer_many" : s_many, "serializer_one" : s_one}

def s_one(request, type, pk):
    if type == "AD":
        obj = annonce_demande.objects.get(pk=pk)
        s_one = Ad_Serializer(obj)
        s_post = Ad_Serializer(obj, data=request.data)
        return {"object" : obj, "serializer_one" : s_one, "serializer_post" : s_post}

    elif type == "AO":
        obj = annonce_offrir.objects.get(pk=pk)
        s_one = Ao_Serializer(obj)
        s_post = Ao_Serializer(obj, data=request.data)
        return {"object" : obj, "serializer_one" : s_one, "serializer_post" : s_post}

    elif type == "L":
        obj = livraison.objects.get(pk=pk)
        s_one = L_Serializer(obj)
        s_post = L_Serializer(obj, data=request.data)
        return {"object" : obj, "serializer_one" : s_one, "serializer_post" : s_post}

    elif type == "AV":
        obj = annonce_ville.objects.get(pk=pk)
        s_one = Av_Serializer(obj)
        s_post = Av_Serializer(obj, data=request.data)
        return {"object" : obj, "serializer_one" : s_one, "serializer_post" : s_post}


class obj_list(APIView):
    """
    list all object related to model and creat a new object
    model = annonce_demande
    """




    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, type, format=None):
        user = request.auth
        print(user)
        try:
            d = which_one(request, type)
            s = d["serializer_many"]
            return Response(s.data)
        except:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, type, format=None):
        user = request.auth
        annonce = annonce_demande(compte=user)
        try:
            d = which_one(request, type)
            s = d["serializer_post"]
            if s.is_valid():
                s.save()
                return Response(s.data, status.HTTP_201_CREATED)
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
        except annonce_demande.DoesNotExist:
            raise  Http404("404!! this is not normal ")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class obj_details(APIView):
    """
    Retrieve, update or delete a snippet instance.
    model = all_classes
    """
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]



    def get(self, request, pk, type, format=None):
        try:
            d = s_one(request, type, pk)
            if haveItOrNot(request,d["object"]) == 11:
                s = d["serializer_one"]
                return Response(s.data)
            else:
                return Response({"permission":"permission denied"})
        except :
            if type not in TYPE_ANNONCE:
                return Response({"bad typing ":"unknown type, im callig FBI  "})
            else:
                return Response({"warnning ...denied_response":"smtg went wrong, im callig FBI  "})


    def put(self, request, pk, type, format=None):
        try:
            d = s_one(request, type, pk)
            if haveItOrNot(request,d["object"]) == 11: # wtvr_class.wtv_serializer(obj, data)
                sp = d["serializer_post"]
                if sp.is_valid():
                    sp.save()
                    return Response(sp.data, {"success":"post saveed"})
                else:
                    return Response({"oups":"validation errors"})
            else:
                return Response({"permission":"permission denied"})
        except:
            return Response({"oups":"smtg went wrong maybe num out of range"})

    def delete(self, request, pk, type, format=None):
        try:
            s = s_one(request, type, pk)
            if haveItOrNot(request,d["object"]):
                s = s["object"]
                s.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"permission":"permission denied"})
        except:
            return Response({"oups":"smtg went wrong"})


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
