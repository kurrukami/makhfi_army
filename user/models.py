from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


#validation functions
def validate_mdp(value):
    if(len(value)<10):
        raise ValidationError("do u want me to hack u ,MDP is too short")
    else:
        return value

def validate_name(value):
    if(len(value)>15):
        raise ValidationError("is that a name or a truck,try a shorter name u dumpass")
    else:
        return value

def first_veri(k):
    if(not k[0].isdigit()):
        if(not k[1].isdigit()):
            return True
        for x in k[2::]:
            if x.isdigit():
                continue
            else:
                return False
        return True
    else:
        return False

def validate_cin(val):
    if first_veri(val):
        s= val.split()
        i=[]
        t=[]
        for x in val :
            if x.isdigit():
                x=int(x)
                i.append(x)
            elif type(x) == str:
                t.append(x)
        if len(i) == 6 and len(t)<=3:
            p = 'positive verification'
            return p
        else:
            n = 'verivication failed, im calling FBI'
            raise ValidationError(n)
    else:
        raise ValidationError('u dumpass r u even a morrocan')



#manager
class compteManager(BaseUserManager):
    def create_user(self, nom, prenom, pseudo, email, CIN, image_profile, password=None ):
        if not nom:
            raise ValidationError("u have a last name don't u")
        if not prenom:
            raise ValidationError("u have a name don't u")
        if not pseudo:
            raise ValidationError("u must have psudo so i can call negga!!")
        if not email:
            raise ValidationError("u email plz ")
        if not CIN:
            raise ValidationError("how do u think we can arrest u if u dt give me ur cin  ")
        if not image_profile:
            raise ValidationError("ist not like i want to see ur face but ...yea u cache me, i want to see it handsom")

        user = self.model(
               email = self.normalize_email(email),
               nom = nom,
               prenom = prenom,
               pseudo = pseudo,
               CIN = CIN,
               image_profile = image_profile,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, pseudo, email, password=None):
        if not pseudo:
            raise ValidationError("u must have psudo so i can call u ... negga!!")

        user = self.model(
               email = self.normalize_email(email),
               pseudo = pseudo,
               password = password,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


#comptes
class compte(AbstractUser):




    nom = models.CharField(max_length=50, validators=[validate_name])
    prenom = models.CharField(max_length=50, validators=[validate_name])
    pseudo = models.SlugField(unique=True)
    image_profile = models.ImageField(upload_to='images/', blank=True)
    CIN = models.CharField(max_length=10, validators=[validate_cin])
    email = models.EmailField(unique=True,)
    #MDP = models.CharField(max_length=30, validators=[validate_mdp])
    visiblty = False
    nutifiction = []


    created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'pseudo'
    REQUIRED_FIELDS = ['email',]

    object = compteManager()

    def delete_cmpt(self):
        if self.visiblty == False:
            self.visiblty = True
        else:
            raise ValidationError("!!! but, wut!!!")


    def get_url(self):
        return f'home/users/{self.pk}/MaybeDumpOne/{self.pseudo}'

    def get_created_time(self):
        msg = '{:%A %B, D%,  time %H:%M:%S.}'
        return msg.format(self.created)

    def get_last_login(self):
        msg = '{:%A %B, D%,  time %H:%M:%S.}'
        return msg.format(self.last_login)


    def __str__(self):
        return f'{self.pseudo}'

    class Meta:
        ordering = ('-created',)
        unique_together = ('email','CIN','pseudo')

# class reclamation
class reclamation(models.Model):

    compte = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reclamation = models.TextField()
    visiblty = False

    def get_url(self):
        return f'home/users/reclamation/{self.compte}/MaybeDumpOne/{self.pk}'
    def __str__(self):
        return f'id: {self.pk} {self.compte}'





@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
