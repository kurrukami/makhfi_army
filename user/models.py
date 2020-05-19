from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist
# Create your models here.


#comptes
class compte(models.Model):

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
    def first_veri(value):
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
    def validate_cin(value):
        if first_veri(value):
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
                raise ValidationError(p)
            else:
                n = 'verivication failed, im calling FBI'
                raise ValidationError(n)
        else:
            raise ValidationError('u dumpass r u even a morrocan')

    nome = models.CharField(max_length=50, validators=[validate_name])
    prénom = models.CharField(max_length=50, validators=[validate_name])
    psudo = models.SlugField(unique=True)
    image_profile = models.ImageField(upload_to='images/')
    CIN = models.CharField(max_length=10, validators=[validate_cin])
    email = models.EmailField(blank=True)
    MDP = models.CharField(max_length=30, validators=[validate_mdp])
    visiblty = False
    nutifiction = []


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def delete_cmpt(self):
        if self.visiblty == False:
            self.visiblty = True
        else:
            raise ValidationError("!!! but, wut!!!")


    def get_url(self):
        return f'home/users/{self.pk}/MaybeDumpOne/{self.psudo}'

    def get_created_time(self):
        msg = '{:%A %B, D%,  time %H:%M:%S.}'
        return msg.format(self.created)

    def get_updated_time(self):
        msg = '{:%A %B, D%,  time %H:%M:%S.}'
        return msg.format(self.updated)


    def __str__(self):
        return f'{self.nome} {self.prénom}'

    class Meta:
        ordering = ('-created',)
        unique_together = ('email','CIN','psudo')

# class reclamation
class reclamation(models.Model):
    compte = models.ForeignKey(compte, on_delete=models.CASCADE)
    reclamation = models.TextField()
    visiblty = False

    def get_url(self):
        return f'home/users/reclamation/{self.compte}/MaybeDumpOne/{self.pk}'
    def __str__(self):
        return f'id: {self.pk} {self.compte}'
