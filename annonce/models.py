from django.db import models
from user.models import compte
from django.core.exceptions import ValidationError
from enum import  Enum

from django.conf import settings

# Create your models here.




#les deffirents datatype

class type_bagages(Enum):

    pas_bgg = ('pas_bgg', 'pas de bagages')
    bgg_normal = ('bgg_normal', 'bagages normal')
    bgg_lourd = ('bgg_lourd', 'bagages lourd')
    bgg_tr_lourd = ('bgg_tr_lourd', 'bagages trés lourd')

    def __str__(self):
        return f'{self.value}'

    @classmethod
    def get_type(cls, type):
        return cls[type].value[1]

class type_service(Enum):

    livreur = ('lvr', 'livreur')
    bagages = ('bgg', 'bagages')

    @classmethod
    def get_type(cls, type):
        return cls[type].value[1]



#les annonces
def validate_num(value):
    if(value<0):
        raise ValidationError("maybe half is better u smartass")
    else:
        return 'value'

#def validate_lieu(self): not corrected yet
#    try:
#        annonce = annonce.self.ville
#    except Exception as e:
#        raise
#    if self.lieu_depart == self.lieu_arrive:
#        raise ValidationError("u sob, u joking right, we r joking now...ha!!")
#    #


#def validate_date(self):  get corrected by me
#    if self.cleaned_data.get("date_depart").day == self.cleaned_data.get("date_arrive").day:
#        if self.cleaned_data.get("date_depart").hour == self.cleaned_data.get("date_arrive").hour:
#            raise ValidationError("u sob, u joking right, we r joking now...ha!!")







class fiche_annonce(models.Model):




    ville_distination = models.CharField(max_length=50)
    lieu_depart = models.CharField(max_length=50)
    lieu_arrive = models.CharField(max_length=50)
    date_depart = models.DateTimeField(max_length=50,)
    date_arrive = models.DateTimeField(max_length=50)
    is_accepted = False
    visiblty = False


    def get_depart(self):
        msg = 'depart : {:%A %B, %d/%m/%Y,  time %H:%M:%S.} '
        print(msg.format(self.date_depart))

    def __str__(self):
        return f'{self.pk}'




class annonce(models.Model):

    #def validate_tele(value):
    #    if len(value)<=10:
    #        raise ValidationError("really nigga, thts ur phone!!")

    compte = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    num_tele = models.IntegerField()
    ville = models.CharField(max_length=30)
    bagages = models.CharField(max_length=12, choices=[x.value for x in type_bagages])
    comment = models.TextField(max_length=200)
    fiche = models.OneToOneField(fiche_annonce, on_delete=models.CASCADE)
    visiblty = False


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}, {self.compte}'

    def get_url(self):
        return f'home/users/{self.pk}/MaybeDumpOne/{self.compte}'

    def get_created_time(self):
        msg = '{:%A %B,  %D, time: %H:%M:%S.} '
        return msg.format(self.created)

    def get_updated_time(self):
        msg = '{:%A %B, %D, time: %H:%M:%S.} '
        return msg.format(self.updated)

    class Meta:
        abstract = True
        ordering = ('-created', 'ville')



#type d annonces
TYPE_ANNONCE = ['AD','AO','AV','L']


#les classes d annonces

class livraison(annonce):

    service = models.CharField(max_length=3, choices=[x.value for x in type_service])
    TYPE = TYPE_ANNONCE[3]

class annonce_demande(annonce):

    num_personnes = models.IntegerField(validators=[validate_num])
    TYPE = TYPE_ANNONCE[0]

class annonce_ville(annonce_demande):

    lieu = models.CharField(max_length=30)
    distination = models.CharField(max_length=30)
    num_places = models.IntegerField(validators=[validate_num])
    date_depart = models.DateField(max_length=50)
    TYPE = TYPE_ANNONCE[2]


class annonce_offrir(annonce):

    num_places = models.IntegerField(validators=[validate_num])
    car_model = models.CharField(max_length=30)
    TYPE = TYPE_ANNONCE[1]
