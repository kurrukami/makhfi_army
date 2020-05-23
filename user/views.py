from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from user.serializers import *

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

# Create your views here.







class obj_list_c(APIView):
    """
    list all object related to model and creat a new object
    model = annonce_demande
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)


    def get(self, request, format=None):
        try:
            t = compte.objects.all()
            s = compte_Serializer(t, many=True)
            return Response(s.data)
        except  :
            raise Http404("404!! this is not normal ")


    def post(self, request, format=None):
        try:
            s = compte_Serializer(data=request.data)
            if s.is_valid():
                s.save()
                return Response(s.data, status.HTTP_201_CREATED)
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
        except compte.DoesNotExist:
            raise  Http404("404!! this is not normal ")


class obj_details_c(APIView):
    """
    Retrieve, update or delete a snippet instance.
    model = annonce_demande
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_obj(self, request, pk):
        try:
            return compte.objects.get(pk=pk)
        except:
            return Response({"response":"i think we don't find shit"})

    def get(self, request, pk, format=None):
        t = self.get_obj(request,pk)
        s = compte_Serializer(t)
        return Response(s.data)

    def put(self, request, pk, format=None):
        t = self.get_obj(request,pk)
        s = compte_Serializer(t, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)

    def delete(self, request, pk, format=None):
        t = self.get_obj(request,pk)
        t.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
