from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("annonce_demande/", views.all_annonce_demande, name="AD"),
    path("annonce_offrir/", views.all_annonce_offrir, name="AO"),
    path("livraison/", views.all_livraison, name="L"),
    path("annonce_ville/", views.all_annonce_ville, name="AV"),
]
