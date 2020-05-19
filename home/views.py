from django.shortcuts import render
from user.models import *
from annonce.models import *
from django.http import HttpResponse
# Create your views here.

CMPT = compte.objects.all()
ANNONCE_DEMANDE = annonce_demande.objects.all()
ANNONCE_OFFRIR = annonce_offrir.objects.all()
LIVRISON = livraison.objects.all()
ANNONCE_VILLE = annonce_ville.objects.all()

LIST_EACH_TYPE = [
    ANNONCE_DEMANDE, ANNONCE_OFFRIR, LIVRISON, ANNONCE_VILLE
]

def search_ville(list_annonce):
    list_ville=[]
    for x in list_annonce:
        if x.ville in list_ville:
            continue
        else:
            list_ville.append(x.ville)
    return list_ville


def filter_ville(ville): #filter ville from d list of each type
    list=[]
    for x in LIST_EACH_TYPE:
        f = lambda i : i.ville == ville
        list.append(filter(f,x))
    return list

def add_nutification(id_annonce, id_sender, add_time):
    try:
        annonce = annonce.objects.get(pk=id_annonce)
        annonce.nutifiction.append({'id_annonce' : (id_sender,add_time)})
    except :
        raise  HttpResponse("<p>sorry handsom, smtg went wrong</p> ")

def clear_nutificatons(id_annonce):
    from datetime import datetime
    try:
        annonce = annonce.objects.get(pk=id_annonce)
        for x in annonce.nutifiction:
            for y in annonce.nutifiction[x]:
                time = annonce.nutifiction[y][1]
                time_now = datetime.now()
                if (time_now.hour-time.hour)>=1:
                    annonce.nutifiction__delitem__(y)
                else:
                    if time_now.day-time.day>=1:
                        annonce.nutifiction__delitem__(y)
                    else:
                        if time_now.mounth-time.mounth>=1:
                            annonce.nutifiction__delitem__(y)
                        else:
                            if time_now.year-time.year>=1:
                                annonce.nutifiction__delitem__(y)
                            else:
                                raise  HttpResponse("!!!wut,  wtf!!! ")
    except :
        raise  HttpResponse("sorry handsom, smtg went wrong ")


def all_cmpt(request):
    return render(request, "test.html", {'CMPT' : CMPT})

def home_page(request):
    return render(request, "home_page.html")

def all_annonce_demande(request):
    list_ville = search_ville(ANNONCE_DEMANDE)
    return render(request, "test.html", {'ANNONCE_DEMANDE' : ANNONCE_DEMANDE, 'list_ville' : list_ville})


def all_annonce_offrir(request):
    return render(request, "test.html", {'ANNONCE_OFFRIR' : ANNONCE_OFFRIR})


def all_livraison(request):
    return render(request, "test.html", {'LIVRISON' : LIVRISON})

def all_annonce_ville(request):
    return render(request, "test.html", {'ANNONCE_VILLE' : ANNONCE_VILLE})
