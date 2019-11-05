from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbour(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # neighbourOccupantsCount=models.IntegerField()
    neighbourNamChoices=(('Amahoro','Amahoro'),
                   ('Agaciro','Agaciro'),
                   ('Intsinzi','Intsinzi'),


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
    businessImage=models.ImageField(upload_to='business/')
    neighbourNamChoices=(('Amahoro','Amahoro'),
                   ('Agaciro','Agaciro'),
                   ('Intsinzi','Intsinzi'),


    )
    businessLocation=models.CharField(max_length=60,choices=neighbourNamChoices)
    neighbourF=models.ForeignKey(Neighbour,on_delete=models.CASCADE)

    def __str__(self):
        return self.businessName
    @classmethod
    def searchBusiness(cls,search_term):
        business = cls.objects.filter(businessName__icontains=search_term)
        return business


class Police(models.Model):
    policeStationName=models.CharField(max_length=30)
    policeEmergencyNbr=models.IntegerField()
    neighbourNamChoices=(('Amahoro','Amahoro'),
                   ('Agaciro','Agaciro'),
                   ('Intsinzi','Intsinzi'),


    )
    policeLocation=models.CharField(max_length=60,choices=neighbourNamChoices)
    neighbourF=models.ForeignKey(Neighbour,on_delete=models.CASCADE)
    policeImage=models.ImageField(upload_to='police/')

    def __str__(self):
        return self.policeStationName


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profileImage=models.ImageField(default='default.jpg',upload_to='profileImg/')
    bio=models.CharField(max_length=100)
    


    def __str__(self):
        return self.user.username



class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    postName=models.CharField(max_length=30)
    postText=models.TextField()
    postImage=models.ImageField(default='default.jpg',upload_to='post/')
    neighbourNamChoices=(('Amahoro','Amahoro'),
                   ('Agaciro','Agaciro'),
                   ('Intsinzi','Intsinzi'),


    )
    postNeighbourName=models.CharField(max_length=60,choices=neighbourNamChoices)
    


    def __str__(self):
        return self.user.username





