from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbour(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # neighbourOccupantsCount=models.IntegerField()
    neighbourNamChoices=(('Kimironko','Kimironko'),
                   ('Nyamirambo','Nyamirambo'),
                   ('Rebero','Rebero'),


    )
    neighbourName=models.CharField(max_length=60,choices=neighbourNamChoices)
    neighbourLocChoices=(('Gasabo','Gasabo'),
                       ('Nyarugenge','Nyarugenge'),
                       ('Kicukiro','Kicukiro'),


    )
    neighbourLocation=models.CharField(max_length=60,choices=neighbourLocChoices)


    def __str__(self):
        return self.user.username

class Business(models.Model):
    businessName=models.CharField(max_length=30)
    businessEmail=models.EmailField()
    neighbourF=models.ForeignKey(Neighbour,on_delete=models.CASCADE)

    def __str__(self):
        return self.businessName


class Police(models.Model):
    policeStationName=models.CharField(max_length=30)
    policeEmergencyNbr=models.IntegerField()
    neighbourF=models.ForeignKey(Neighbour,on_delete=models.CASCADE)

    def __str__(self):
        return self.policeStationName


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profileImage=models.ImageField(default='default.jpg',upload_to='profileImg/')
    bio=models.CharField(max_length=100)
    


    def __str__(self):
        return self.user.username




